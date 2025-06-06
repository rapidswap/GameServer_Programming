"""
점진적 부하테스트 시나리오 관리자
다양한 부하 증가 패턴을 지원하는 고급 테스트 도구
"""

import time
import threading
import logging
from typing import List, Dict, Any, Callable
from dataclasses import dataclass
from enum import Enum
from load_test_manager import LoadTestManager


class LoadPattern(Enum):
    """부하 증가 패턴"""
    LINEAR = "linear"           # 선형 증가
    EXPONENTIAL = "exponential" # 지수적 증가  
    STEP = "step"              # 단계적 증가
    SPIKE = "spike"            # 급증 테스트
    RAMP_UP_DOWN = "ramp_up_down"  # 증가 후 감소
    SUSTAINED = "sustained"    # 지속적 부하
    STRESS = "stress"          # 스트레스 테스트


@dataclass
class LoadScenario:
    """부하테스트 시나리오"""
    name: str
    pattern: LoadPattern
    start_bots: int
    max_bots: int
    step_size: int
    step_duration: int  # 각 단계 지속시간(초)
    total_duration: int = 0  # 전체 테스트 시간(초), 0이면 무제한
    description: str = ""


class ProgressiveLoadTester:
    """점진적 부하테스트 관리자"""
    
    def __init__(self, server_host: str = "localhost", server_port: int = 9200):
        self.server_host = server_host
        self.server_port = server_port
        
        # 매니저 및 상태
        self.manager = LoadTestManager(server_host, server_port)
        self.running = False
        self.current_scenario: LoadScenario = None
        self.current_bot_count = 0
        
        # 통계 및 모니터링
        self.scenario_stats = []
        self.performance_metrics = []
        self.failure_threshold = 0.1  # 10% 실패율에서 중단
        
        # 스레드
        self.test_thread: threading.Thread = None
        
        # 로깅
        self.logger = logging.getLogger("ProgressiveLoadTester")
        
        # 콜백
        self.step_callback: Callable = None
        self.failure_callback: Callable = None
    
    def add_step_callback(self, callback: Callable):
        """단계 변경 시 콜백 등록"""
        self.step_callback = callback
    
    def add_failure_callback(self, callback: Callable):
        """실패 임계값 도달 시 콜백 등록"""
        self.failure_callback = callback
    
    def get_predefined_scenarios(self) -> List[LoadScenario]:
        """사전 정의된 시나리오 목록"""
        return [
            LoadScenario(
                name="웜업 테스트",
                pattern=LoadPattern.LINEAR,
                start_bots=1,
                max_bots=10,
                step_size=1,
                step_duration=30,
                description="1개부터 10개까지 선형 증가, 각 단계 30초"
            ),
            LoadScenario(
                name="기본 부하테스트",
                pattern=LoadPattern.STEP,
                start_bots=5,
                max_bots=50,
                step_size=5,
                step_duration=60,
                description="5개부터 50개까지 5개씩 증가, 각 단계 60초"
            ),
            LoadScenario(
                name="지수적 증가",
                pattern=LoadPattern.EXPONENTIAL,
                start_bots=1,
                max_bots=64,
                step_size=2,  # 배수
                step_duration=45,
                description="1, 2, 4, 8, 16, 32, 64개로 지수적 증가"
            ),
            LoadScenario(
                name="스파이크 테스트",
                pattern=LoadPattern.SPIKE,
                start_bots=10,
                max_bots=100,
                step_size=90,  # 한번에 90개 증가
                step_duration=120,
                description="10개에서 100개로 급증 후 2분 유지"
            ),
            LoadScenario(
                name="램프업/다운",
                pattern=LoadPattern.RAMP_UP_DOWN,
                start_bots=5,
                max_bots=40,
                step_size=5,
                step_duration=30,
                total_duration=600,  # 10분
                description="증가 후 감소하는 패턴"
            ),
            LoadScenario(
                name="지속적 부하",
                pattern=LoadPattern.SUSTAINED,
                start_bots=20,
                max_bots=20,
                step_size=0,
                step_duration=300,  # 5분
                description="20개 봇으로 5분간 지속"
            ),
            LoadScenario(
                name="스트레스 테스트",
                pattern=LoadPattern.STRESS,
                start_bots=10,
                max_bots=200,
                step_size=10,
                step_duration=45,
                description="한계점까지 계속 증가"
            )
        ]
    
    def run_scenario(self, scenario: LoadScenario) -> bool:
        """시나리오 실행"""
        if self.running:
            self.logger.warning("Test already running")
            return False
        
        self.running = True
        self.current_scenario = scenario
        self.scenario_stats = []
        self.performance_metrics = []
        
        self.logger.info(f"Starting scenario: {scenario.name}")
        self.logger.info(f"Description: {scenario.description}")
        
        self.test_thread = threading.Thread(target=self._run_scenario_thread, daemon=True)
        self.test_thread.start()
        
        return True
    
    def stop_scenario(self):
        """시나리오 중지"""
        self.running = False
        if self.manager.test_running:
            self.manager.stop_test()
        self.logger.info("Scenario stopped by user")
    
    def _run_scenario_thread(self):
        """시나리오 실행 스레드"""
        try:
            scenario = self.current_scenario
            
            if scenario.pattern == LoadPattern.LINEAR:
                self._run_linear_pattern(scenario)
            elif scenario.pattern == LoadPattern.EXPONENTIAL:
                self._run_exponential_pattern(scenario)
            elif scenario.pattern == LoadPattern.STEP:
                self._run_step_pattern(scenario)
            elif scenario.pattern == LoadPattern.SPIKE:
                self._run_spike_pattern(scenario)
            elif scenario.pattern == LoadPattern.RAMP_UP_DOWN:
                self._run_ramp_up_down_pattern(scenario)
            elif scenario.pattern == LoadPattern.SUSTAINED:
                self._run_sustained_pattern(scenario)
            elif scenario.pattern == LoadPattern.STRESS:
                self._run_stress_pattern(scenario)
            
        except Exception as e:
            self.logger.error(f"Scenario execution error: {e}")
        finally:
            self.running = False
            if self.manager.test_running:
                self.manager.stop_test()
            self.logger.info("Scenario completed")
    
    def _run_linear_pattern(self, scenario: LoadScenario):
        """선형 증가 패턴"""
        current_bots = scenario.start_bots
        
        while self.running and current_bots <= scenario.max_bots:
            self._execute_step(current_bots, scenario.step_duration)
            
            if not self.running:
                break
                
            current_bots += scenario.step_size
    
    def _run_exponential_pattern(self, scenario: LoadScenario):
        """지수적 증가 패턴"""
        current_bots = scenario.start_bots
        
        while self.running and current_bots <= scenario.max_bots:
            self._execute_step(current_bots, scenario.step_duration)
            
            if not self.running:
                break
                
            current_bots *= scenario.step_size
            if current_bots > scenario.max_bots:
                current_bots = scenario.max_bots
    
    def _run_step_pattern(self, scenario: LoadScenario):
        """단계적 증가 패턴"""
        current_bots = scenario.start_bots
        
        while self.running and current_bots <= scenario.max_bots:
            self._execute_step(current_bots, scenario.step_duration)
            
            if not self.running:
                break
                
            current_bots += scenario.step_size
    
    def _run_spike_pattern(self, scenario: LoadScenario):
        """급증 패턴"""
        # 초기 부하
        self._execute_step(scenario.start_bots, scenario.step_duration // 3)
        
        if not self.running:
            return
            
        # 급증
        self._execute_step(scenario.max_bots, scenario.step_duration)
        
        if not self.running:
            return
            
        # 복구
        self._execute_step(scenario.start_bots, scenario.step_duration // 3)
    
    def _run_ramp_up_down_pattern(self, scenario: LoadScenario):
        """증가 후 감소 패턴"""
        start_time = time.time()
        half_duration = scenario.total_duration // 2 if scenario.total_duration > 0 else 300
        
        # 증가 단계
        current_bots = scenario.start_bots
        while self.running and current_bots <= scenario.max_bots:
            if time.time() - start_time > half_duration:
                break
                
            self._execute_step(current_bots, scenario.step_duration)
            current_bots += scenario.step_size
        
        # 감소 단계
        while self.running and current_bots >= scenario.start_bots:
            if scenario.total_duration > 0 and time.time() - start_time > scenario.total_duration:
                break
                
            self._execute_step(current_bots, scenario.step_duration)
            current_bots -= scenario.step_size
    
    def _run_sustained_pattern(self, scenario: LoadScenario):
        """지속적 부하 패턴"""
        self._execute_step(scenario.start_bots, scenario.step_duration)
    
    def _run_stress_pattern(self, scenario: LoadScenario):
        """스트레스 테스트 패턴 - 실패까지 계속 증가"""
        current_bots = scenario.start_bots
        
        while self.running:
            self._execute_step(current_bots, scenario.step_duration)
            
            # 실패율 확인
            stats = self.manager.get_current_stats()
            if self._check_failure_threshold(stats):
                self.logger.warning(f"Failure threshold reached at {current_bots} bots")
                if self.failure_callback:
                    self.failure_callback(current_bots, stats)
                break
            
            current_bots += scenario.step_size
            
            # 최대값 제한 (무한 증가 방지)
            if current_bots > scenario.max_bots:
                self.logger.info(f"Maximum bot limit ({scenario.max_bots}) reached")
                break
    
    def _execute_step(self, bot_count: int, duration: int):
        """단일 단계 실행"""
        if not self.running:
            return
            
        self.current_bot_count = bot_count
        self.logger.info(f"Step: {bot_count} bots for {duration} seconds")
        
        # 봇 생성 및 테스트 시작
        if not self.manager.create_bots(bot_count):
            self.logger.error(f"Failed to create {bot_count} bots")
            return
        
        if not self.manager.start_test(duration):
            self.logger.error("Failed to start test")
            return
        
        # 단계 시작 콜백
        if self.step_callback:
            self.step_callback(bot_count, duration)
        
        # 단계 완료까지 대기
        start_time = time.time()
        while self.running and self.manager.test_running:
            time.sleep(1)
            
            # 시간 초과 확인
            if time.time() - start_time > duration + 5:  # 5초 여유
                break
        
        # 통계 수집
        stats = self.manager.get_current_stats()
        step_stats = {
            'bot_count': bot_count,
            'duration': duration,
            'timestamp': time.time(),
            'stats': stats.copy()
        }
        self.scenario_stats.append(step_stats)
        
        # 테스트 중지
        if self.manager.test_running:
            self.manager.stop_test()
        
        # 다음 단계 전 잠시 대기
        if self.running:
            time.sleep(2)
    
    def _check_failure_threshold(self, stats: Dict) -> bool:
        """실패 임계값 확인"""
        if not stats or stats['connected_bots'] == 0:
            return True
        
        # 연결 실패율 확인
        connection_failure_rate = stats['error_count'] / stats['total_bots']
        if connection_failure_rate > self.failure_threshold:
            return True
        
        # 응답 없는 봇 비율 확인
        if stats['total_bots'] > 0:
            unresponsive_rate = (stats['total_bots'] - stats['connected_bots']) / stats['total_bots']
            if unresponsive_rate > self.failure_threshold:
                return True
        
        return False
    
    def get_scenario_report(self) -> Dict[str, Any]:
        """시나리오 실행 결과 리포트"""
        if not self.scenario_stats:
            return {}
        
        report = {
            'scenario': {
                'name': self.current_scenario.name,
                'pattern': self.current_scenario.pattern.value,
                'description': self.current_scenario.description
            },
            'execution': {
                'total_steps': len(self.scenario_stats),
                'max_bots_tested': max(step['bot_count'] for step in self.scenario_stats),
                'total_duration': sum(step['duration'] for step in self.scenario_stats)
            },
            'performance': {
                'peak_throughput': 0,
                'peak_concurrent_users': 0,
                'avg_response_time': 0,
                'error_rate': 0
            },
            'steps': self.scenario_stats
        }
        
        # 성능 메트릭 계산
        if self.scenario_stats:
            peak_throughput = 0
            peak_concurrent = 0
            total_errors = 0
            total_bots = 0
            
            for step in self.scenario_stats:
                stats = step['stats']
                if stats['elapsed_time'] > 0:
                    throughput = stats['messages_sent'] / stats['elapsed_time']
                    peak_throughput = max(peak_throughput, throughput)
                
                peak_concurrent = max(peak_concurrent, stats['connected_bots'])
                total_errors += stats['error_count']
                total_bots += stats['total_bots']
            
            report['performance']['peak_throughput'] = peak_throughput
            report['performance']['peak_concurrent_users'] = peak_concurrent
            if total_bots > 0:
                report['performance']['error_rate'] = total_errors / total_bots
        
        return report
    
    def export_scenario_report(self, filename: str = None) -> str:
        """시나리오 리포트 내보내기"""
        if not filename:
            from datetime import datetime
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            scenario_name = self.current_scenario.name.replace(' ', '_') if self.current_scenario else 'scenario'
            filename = f"progressive_test_{scenario_name}_{timestamp}.json"
        
        report = self.get_scenario_report()
        
        try:
            import json
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2, ensure_ascii=False)
            
            self.logger.info(f"Scenario report exported to {filename}")
            return filename
            
        except Exception as e:
            self.logger.error(f"Failed to export report: {e}")
            return ""
    
    def print_progress_report(self):
        """진행 상황 리포트 출력"""
        if not self.scenario_stats:
            print("진행 상황 데이터가 없습니다.")
            return
        
        print("\n" + "="*80)
        print(f"점진적 부하테스트 진행 상황 - {self.current_scenario.name}")
        print("="*80)
        
        for i, step in enumerate(self.scenario_stats, 1):
            stats = step['stats']
            print(f"단계 {i}: {step['bot_count']}개 봇")
            print(f"  연결된 봇: {stats['connected_bots']}/{stats['total_bots']}")
            print(f"  메시지: 전송 {stats['messages_sent']}, 수신 {stats['messages_received']}")
            print(f"  오류: {stats['error_count']}")
            
            if stats['elapsed_time'] > 0:
                throughput = stats['messages_sent'] / stats['elapsed_time']
                print(f"  처리량: {throughput:.1f} 메시지/초")
            print()
