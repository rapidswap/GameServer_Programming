"""
적응형 부하테스트 - 서버 성능에 따라 자동으로 부하를 조절
"""

import time
import threading
import psutil
import logging
from typing import Dict, List, Optional, Callable
from dataclasses import dataclass
from progressive_load_tester import ProgressiveLoadTester, LoadScenario, LoadPattern


@dataclass
class PerformanceThresholds:
    """성능 임계값 설정"""
    max_cpu_percent: float = 80.0        # CPU 사용률 상한
    max_memory_percent: float = 85.0     # 메모리 사용률 상한
    max_response_time_ms: float = 1000.0 # 응답시간 상한(ms)
    min_success_rate: float = 0.95       # 최소 성공률 (95%)
    max_error_rate: float = 0.05         # 최대 오류율 (5%)


class AdaptiveLoadTester:
    """적응형 부하테스트 - 서버 성능 기반 자동 조절"""
    
    def __init__(self, server_host: str = "localhost", server_port: int = 9200,
                 process_name: str = "ChattingServer.exe"):
        self.server_host = server_host
        self.server_port = server_port
        self.process_name = process_name
        
        # 기본 테스터
        self.base_tester = ProgressiveLoadTester(server_host, server_port)
        
        # 성능 모니터링
        self.server_process: Optional[psutil.Process] = None
        self.thresholds = PerformanceThresholds()
        self.monitoring_interval = 5.0  # 5초마다 성능 체크
        
        # 적응형 제어
        self.running = False
        self.current_bots = 0
        self.max_stable_bots = 0  # 안정적으로 처리할 수 있는 최대 봇 수
        self.performance_history: List[Dict] = []
        
        # 자동 조절 설정
        self.auto_scale_enabled = True
        self.scale_up_factor = 1.2    # 20% 증가
        self.scale_down_factor = 0.8  # 20% 감소
        self.min_bots = 1
        self.max_bots = 200
        self.stable_duration = 30     # 30초간 안정적이면 증가
        
        # 스레드
        self.monitor_thread: Optional[threading.Thread] = None
        self.control_thread: Optional[threading.Thread] = None
        
        # 콜백
        self.performance_callback: Optional[Callable] = None
        self.scale_callback: Optional[Callable] = None
        
        # 로깅
        self.logger = logging.getLogger("AdaptiveLoadTester")
    
    def set_thresholds(self, thresholds: PerformanceThresholds):
        """성능 임계값 설정"""
        self.thresholds = thresholds
    
    def find_server_process(self) -> bool:
        """서버 프로세스 찾기"""
        try:
            for proc in psutil.process_iter(['pid', 'name']):
                if self.process_name.lower() in proc.info['name'].lower():
                    self.server_process = psutil.Process(proc.info['pid'])
                    self.logger.info(f"Server process found: PID {proc.info['pid']}")
                    return True
            
            self.logger.warning(f"Server process '{self.process_name}' not found")
            return False
            
        except Exception as e:
            self.logger.error(f"Error finding server process: {e}")
            return False
    
    def start_adaptive_test(self, initial_bots: int = 5) -> bool:
        """적응형 테스트 시작"""
        if self.running:
            self.logger.warning("Test already running")
            return False
        
        if not self.find_server_process():
            self.logger.error("Cannot start test without server process")
            return False
        
        self.running = True
        self.current_bots = initial_bots
        self.max_stable_bots = 0
        self.performance_history = []
        
        self.logger.info(f"Starting adaptive load test with {initial_bots} bots")
        
        # 초기 봇 생성 및 시작
        if not self.base_tester.create_bots(initial_bots):
            self.logger.error(f"Failed to create {initial_bots} bots")
            self.running = False
            return False
        
        if not self.base_tester.start_test(0):  # 무제한 시간
            self.logger.error("Failed to start base test")
            self.running = False
            return False
        
        # 모니터링 및 제어 스레드 시작
        self.monitor_thread = threading.Thread(target=self._monitoring_loop, daemon=True)
        self.monitor_thread.start()
        
        self.control_thread = threading.Thread(target=self._control_loop, daemon=True)
        self.control_thread.start()
        
        return True
    
    def stop_adaptive_test(self):
        """적응형 테스트 중지"""
        self.running = False
        if self.base_tester.test_running:
            self.base_tester.stop_test()
        self.logger.info("Adaptive test stopped")
    
    def _monitoring_loop(self):
        """성능 모니터링 루프"""
        while self.running:
            try:
                performance_data = self._collect_performance_data()
                if performance_data:
                    self.performance_history.append(performance_data)
                    
                    # 최근 100개 데이터만 유지
                    if len(self.performance_history) > 100:
                        self.performance_history = self.performance_history[-100:]
                    
                    # 성능 콜백 호출
                    if self.performance_callback:
                        self.performance_callback(performance_data)
                
                time.sleep(self.monitoring_interval)
                
            except Exception as e:
                self.logger.error(f"Monitoring loop error: {e}")
                time.sleep(self.monitoring_interval)
    
    def _control_loop(self):
        """자동 제어 루프"""
        last_scale_time = time.time()
        stable_start_time = time.time()
        
        while self.running:
            try:
                time.sleep(10)  # 10초마다 제어 결정
                
                if not self.auto_scale_enabled:
                    continue
                
                current_time = time.time()
                
                # 최근 성능 데이터 분석
                decision = self._make_scaling_decision()
                
                if decision == "scale_up":
                    # 30초간 안정적이었다면 증가
                    if current_time - stable_start_time >= self.stable_duration:
                        new_bot_count = min(int(self.current_bots * self.scale_up_factor), self.max_bots)
                        if new_bot_count > self.current_bots:
                            self._scale_bots(new_bot_count)
                            last_scale_time = current_time
                            stable_start_time = current_time  # 안정성 타이머 리셋
                
                elif decision == "scale_down":
                    # 즉시 감소
                    new_bot_count = max(int(self.current_bots * self.scale_down_factor), self.min_bots)
                    if new_bot_count < self.current_bots:
                        self._scale_bots(new_bot_count)
                        last_scale_time = current_time
                        stable_start_time = current_time  # 안정성 타이머 리셋
                
                elif decision == "stable":
                    # 안정적인 상태 유지
                    pass
                
            except Exception as e:
                self.logger.error(f"Control loop error: {e}")
    
    def _collect_performance_data(self) -> Optional[Dict]:
        """성능 데이터 수집"""
        try:
            timestamp = time.time()
            
            # 시스템 메트릭
            cpu_percent = psutil.cpu_percent(interval=1.0)
            memory = psutil.virtual_memory()
            
            # 서버 프로세스 메트릭
            process_metrics = {}
            if self.server_process and self.server_process.is_running():
                try:
                    process_metrics = {
                        'cpu_percent': self.server_process.cpu_percent(),
                        'memory_percent': self.server_process.memory_percent(),
                        'num_threads': self.server_process.num_threads(),
                        'connections': len(self.server_process.connections())
                    }
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    self.logger.warning("Lost access to server process")
                    return None
            
            # 부하테스트 메트릭
            test_stats = self.base_tester.get_current_stats()
            
            # 응답시간 계산 (간단한 추정)
            avg_response_time = 0.0
            if test_stats.get('latency') and test_stats['latency'].get('avg'):
                avg_response_time = test_stats['latency']['avg']
            
            # 성공률 계산
            success_rate = 1.0
            if test_stats['total_bots'] > 0:
                success_rate = test_stats['connected_bots'] / test_stats['total_bots']
            
            # 오류율 계산
            error_rate = 0.0
            if test_stats['total_bots'] > 0:
                error_rate = test_stats['error_count'] / test_stats['total_bots']
            
            return {
                'timestamp': timestamp,
                'current_bots': self.current_bots,
                'system': {
                    'cpu_percent': cpu_percent,
                    'memory_percent': memory.percent
                },
                'process': process_metrics,
                'application': {
                    'response_time_ms': avg_response_time,
                    'success_rate': success_rate,
                    'error_rate': error_rate,
                    'connected_bots': test_stats['connected_bots'],
                    'messages_per_sec': test_stats['messages_sent'] / max(test_stats['elapsed_time'], 1)
                }
            }
            
        except Exception as e:
            self.logger.error(f"Error collecting performance data: {e}")
            return None
    
    def _make_scaling_decision(self) -> str:
        """스케일링 결정 로직"""
        if len(self.performance_history) < 3:
            return "stable"  # 충분한 데이터가 없음
        
        # 최근 3개 데이터의 평균
        recent_data = self.performance_history[-3:]
        
        avg_cpu = sum(d['system']['cpu_percent'] for d in recent_data) / len(recent_data)
        avg_memory = sum(d['system']['memory_percent'] for d in recent_data) / len(recent_data)
        avg_success_rate = sum(d['application']['success_rate'] for d in recent_data) / len(recent_data)
        avg_error_rate = sum(d['application']['error_rate'] for d in recent_data) / len(recent_data)
        
        # 응답시간 (사용 가능한 경우)
        avg_response_time = sum(d['application']['response_time_ms'] for d in recent_data) / len(recent_data)
        
        # 스케일 다운 조건 (우선순위 높음)
        if (avg_cpu > self.thresholds.max_cpu_percent or
            avg_memory > self.thresholds.max_memory_percent or
            avg_success_rate < self.thresholds.min_success_rate or
            avg_error_rate > self.thresholds.max_error_rate or
            avg_response_time > self.thresholds.max_response_time_ms):
            
            self.logger.warning(f"Performance degradation detected: "
                              f"CPU={avg_cpu:.1f}%, Memory={avg_memory:.1f}%, "
                              f"Success={avg_success_rate:.2f}, Error={avg_error_rate:.2f}, "
                              f"ResponseTime={avg_response_time:.1f}ms")
            return "scale_down"
        
        # 스케일 업 조건
        if (avg_cpu < self.thresholds.max_cpu_percent * 0.7 and  # CPU 70% 이하
            avg_memory < self.thresholds.max_memory_percent * 0.7 and  # 메모리 70% 이하
            avg_success_rate >= self.thresholds.min_success_rate and
            avg_error_rate <= self.thresholds.max_error_rate * 0.5 and  # 오류율 절반 이하
            avg_response_time < self.thresholds.max_response_time_ms * 0.5):  # 응답시간 절반 이하
            
            return "scale_up"
        
        return "stable"
    
    def _scale_bots(self, new_bot_count: int):
        """봇 수 조절"""
        old_count = self.current_bots
        
        try:
            # 기존 테스트 중지
            if self.base_tester.test_running:
                self.base_tester.stop_test()
            
            time.sleep(2)  # 잠시 대기
            
            # 새로운 봇 수로 테스트 시작
            if self.base_tester.create_bots(new_bot_count):
                if self.base_tester.start_test(0):  # 무제한 시간
                    self.current_bots = new_bot_count
                    
                    # 최대 안정 봇 수 업데이트
                    if new_bot_count > old_count:
                        self.max_stable_bots = new_bot_count
                    
                    action = "증가" if new_bot_count > old_count else "감소"
                    self.logger.info(f"봇 수 {action}: {old_count} → {new_bot_count}")
                    
                    # 스케일링 콜백 호출
                    if self.scale_callback:
                        self.scale_callback(old_count, new_bot_count, action)
                    
                    return True
            
            self.logger.error(f"Failed to scale to {new_bot_count} bots")
            return False
            
        except Exception as e:
            self.logger.error(f"Error scaling bots: {e}")
            return False
    
    def print_current_status(self):
        """현재 상태 출력"""
        if not self.performance_history:
            print("성능 데이터가 없습니다.")
            return
        
        latest = self.performance_history[-1]
        
        print("\n" + "="*60)
        print("적응형 부하테스트 상태")
        print("="*60)
        print(f"현재 봇 수: {self.current_bots}")
        print(f"최대 안정 봇 수: {self.max_stable_bots}")
        print(f"시스템 CPU: {latest['system']['cpu_percent']:.1f}%")
        print(f"시스템 메모리: {latest['system']['memory_percent']:.1f}%")
        
        if latest['process']:
            print(f"서버 CPU: {latest['process']['cpu_percent']:.1f}%")
            print(f"서버 메모리: {latest['process']['memory_percent']:.1f}%")
            print(f"연결 수: {latest['process']['connections']}")
        
        app = latest['application']
        print(f"성공률: {app['success_rate']:.2%}")
        print(f"오류율: {app['error_rate']:.2%}")
        print(f"응답시간: {app['response_time_ms']:.1f}ms")
        print(f"처리량: {app['messages_per_sec']:.1f} 메시지/초")


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="적응형 채팅서버 부하테스트")
    parser.add_argument("--host", default="localhost", help="서버 호스트")
    parser.add_argument("--port", type=int, default=9200, help="서버 포트")
    parser.add_argument("--process", default="ChattingServer.exe", help="모니터링할 프로세스명")
    parser.add_argument("--initial-bots", type=int, default=5, help="초기 봇 수")
    parser.add_argument("--max-bots", type=int, default=200, help="최대 봇 수")
    parser.add_argument("--duration", type=int, help="테스트 시간(초)")
    
    args = parser.parse_args()
    
    # 적응형 테스터 생성
    tester = AdaptiveLoadTester(args.host, args.port, args.process)
    tester.max_bots = args.max_bots
    
    # 콜백 설정
    def performance_callback(data):
        if len(tester.performance_history) % 12 == 0:  # 1분마다 출력
            tester.print_current_status()
    
    def scale_callback(old_count, new_count, action):
        print(f"\n🔄 봇 수 {action}: {old_count} → {new_count}")
    
    tester.performance_callback = performance_callback
    tester.scale_callback = scale_callback
    
    print(f"적응형 부하테스트 시작 - 초기 봇: {args.initial_bots}, 최대 봇: {args.max_bots}")
    
    try:
        if tester.start_adaptive_test(args.initial_bots):
            start_time = time.time()
            
            while tester.running:
                time.sleep(1)
                
                # 시간 제한 확인
                if args.duration and time.time() - start_time > args.duration:
                    print(f"\n테스트 시간 {args.duration}초 완료")
                    break
        else:
            print("적응형 테스트 시작 실패")
    
    except KeyboardInterrupt:
        print("\n테스트 중지됨")
    
    finally:
        tester.stop_adaptive_test()
        tester.print_current_status()
        
        # 리포트 저장
        report_file = tester.export_adaptive_report()
        if report_file:
            print(f"결과가 {report_file}에 저장되었습니다.")
