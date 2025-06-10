"""
점진적 부하테스트 실행기
"""

import argparse
import time
import signal
import sys
from progressive_load_tester import ProgressiveLoadTester, LoadScenario, LoadPattern


class ProgressiveTestRunner:
    """점진적 부하테스트 실행기"""
    
    def __init__(self):
        self.tester = None
        self.running = True
    
    def signal_handler(self, signum, frame):
        """시그널 핸들러 (Ctrl+C 처리)"""
        print("\n테스트 중지 중...")
        self.running = False
        if self.tester:
            self.tester.stop_scenario()
        sys.exit(0)
    
    def step_callback(self, bot_count: int, duration: int):
        """단계 변경 콜백"""
        print(f"\n🔄 새 단계 시작: {bot_count}개 봇으로 {duration}초간 테스트")
    
    def failure_callback(self, bot_count: int, stats: dict):
        """실패 임계값 도달 콜백"""
        print(f"\n⚠️  실패 임계값 도달! {bot_count}개 봇에서 한계 도달")
        print(f"연결 실패: {stats['error_count']}, 총 봇: {stats['total_bots']}")
    
    def run_interactive_mode(self, tester: ProgressiveLoadTester):
        """대화형 모드"""
        print("\n=== 점진적 채팅서버 부하테스트 ===")
        print("사용 가능한 명령어:")
        print("  list                          - 사전정의 시나리오 목록")
        print("  run <시나리오번호>             - 시나리오 실행")
        print("  custom                        - 사용자 정의 시나리오")
        print("  status                        - 현재 상태")
        print("  report                        - 진행 상황 리포트")
        print("  export [파일명]               - 결과 내보내기")
        print("  stop                          - 현재 테스트 중지")
        print("  quit                          - 프로그램 종료")
        print()
        
        scenarios = tester.get_predefined_scenarios()
        
        while self.running:
            try:
                cmd = input("명령어 입력> ").strip().split()
                if not cmd:
                    continue
                
                command = cmd[0].lower()
                
                if command == "list":
                    self._list_scenarios(scenarios)
                
                elif command == "run":
                    if len(cmd) < 2:
                        print("사용법: run <시나리오번호>")
                        continue
                    
                    try:
                        scenario_idx = int(cmd[1]) - 1
                        if 0 <= scenario_idx < len(scenarios):
                            scenario = scenarios[scenario_idx]
                            print(f"시나리오 실행: {scenario.name}")
                            print(f"설명: {scenario.description}")
                            
                            if tester.run_scenario(scenario):
                                print("시나리오가 시작되었습니다.")
                            else:
                                print("시나리오 시작 실패")
                        else:
                            print("올바른 시나리오 번호를 입력하세요.")
                    except ValueError:
                        print("올바른 숫자를 입력하세요.")
                
                elif command == "custom":
                    self._create_custom_scenario(tester)
                
                elif command == "status":
                    if tester.running:
                        print(f"실행 중: {tester.current_scenario.name if tester.current_scenario else 'Unknown'}")
                        print(f"현재 봇 수: {tester.current_bot_count}")
                    else:
                        print("실행 중인 테스트가 없습니다.")
                
                elif command == "report":
                    tester.print_progress_report()
                
                elif command == "export":
                    filename = cmd[1] if len(cmd) > 1 else None
                    exported_file = tester.export_scenario_report(filename)
                    if exported_file:
                        print(f"결과가 {exported_file}에 저장되었습니다.")
                
                elif command == "stop":
                    if tester.running:
                        tester.stop_scenario()
                        print("테스트가 중지되었습니다.")
                    else:
                        print("실행 중인 테스트가 없습니다.")
                
                elif command == "quit" or command == "exit":
                    if tester.running:
                        print("테스트를 먼저 중지합니다...")
                        tester.stop_scenario()
                    break
                
                else:
                    print(f"알 수 없는 명령어: {command}")
                    
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"명령어 처리 중 오류: {e}")
        
        print("프로그램을 종료합니다.")
    
    def _list_scenarios(self, scenarios):
        """시나리오 목록 출력"""
        print("\n사전 정의된 시나리오:")
        print("-" * 60)
        for i, scenario in enumerate(scenarios, 1):
            print(f"{i}. {scenario.name}")
            print(f"   패턴: {scenario.pattern.value}")
            print(f"   봇 수: {scenario.start_bots} → {scenario.max_bots} (단계: {scenario.step_size})")
            print(f"   단계 시간: {scenario.step_duration}초")
            print(f"   설명: {scenario.description}")
            print()
    
    def _create_custom_scenario(self, tester):
        """사용자 정의 시나리오 생성"""
        try:
            print("\n사용자 정의 시나리오 생성")
            
            name = input("시나리오 이름: ").strip() or "Custom Test"
            
            print("패턴 선택:")
            patterns = list(LoadPattern)
            for i, pattern in enumerate(patterns, 1):
                print(f"  {i}. {pattern.value}")
            
            pattern_idx = int(input("패턴 번호: ")) - 1
            if not (0 <= pattern_idx < len(patterns)):
                print("올바른 패턴 번호를 입력하세요.")
                return
            
            pattern = patterns[pattern_idx]
            start_bots = int(input("시작 봇 수: ") or "1")
            max_bots = int(input("최대 봇 수: ") or "20")
            step_size = int(input("단계 크기: ") or "1")
            step_duration = int(input("단계 지속시간(초): ") or "30")
            
            scenario = LoadScenario(
                name=name,
                pattern=pattern,
                start_bots=start_bots,
                max_bots=max_bots,
                step_size=step_size,
                step_duration=step_duration,
                description=f"사용자 정의: {start_bots}→{max_bots} 봇"
            )
            
            print(f"\n시나리오 생성됨: {scenario.name}")
            print(f"실행하시겠습니까? (y/n): ", end="")
            
            if input().lower().startswith('y'):
                if tester.run_scenario(scenario):
                    print("시나리오가 시작되었습니다.")
                else:
                    print("시나리오 시작 실패")
            
        except ValueError:
            print("올바른 숫자를 입력하세요.")
        except Exception as e:
            print(f"시나리오 생성 오류: {e}")
    
    def run_batch_mode(self, args):
        """배치 모드 실행"""
        tester = ProgressiveLoadTester(args.host, args.port)
        tester.add_step_callback(self.step_callback)
        tester.add_failure_callback(self.failure_callback)
        
        # 시나리오 생성
        if args.scenario:
            scenarios = tester.get_predefined_scenarios()
            try:
                scenario_idx = int(args.scenario) - 1
                if 0 <= scenario_idx < len(scenarios):
                    scenario = scenarios[scenario_idx]
                else:
                    print(f"올바른 시나리오 번호를 입력하세요 (1-{len(scenarios)})")
                    return 1
            except ValueError:
                print("올바른 시나리오 번호를 입력하세요.")
                return 1
        else:
            # 사용자 정의 시나리오
            scenario = LoadScenario(
                name="Batch Test",
                pattern=LoadPattern.STEP,
                start_bots=args.start_bots,
                max_bots=args.max_bots,
                step_size=args.step_size,
                step_duration=args.step_duration
            )
        
        print(f"배치 모드: {scenario.name}")
        print(f"설명: {scenario.description}")
        
        # 시나리오 실행
        if not tester.run_scenario(scenario):
            print("시나리오 시작 실패")
            return 1
        
        # 완료까지 대기
        try:
            while tester.running:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n테스트 중지됨")
            tester.stop_scenario()
        
        # 최종 리포트
        print("\n=== 최종 테스트 결과 ===")
        tester.print_progress_report()
        
        # 결과 저장
        if args.output:
            tester.export_scenario_report(args.output)
        
        return 0
    
    def main(self):
        """메인 함수"""
        parser = argparse.ArgumentParser(description="점진적 채팅서버 부하테스트")
        parser.add_argument("--host", default="localhost", help="서버 호스트")
        parser.add_argument("--port", type=int, default=9200, help="서버 포트")
        
        # 배치 모드 옵션
        parser.add_argument("--scenario", help="사전정의 시나리오 번호 (1-7)")
        parser.add_argument("--start-bots", type=int, default=1, help="시작 봇 수")
        parser.add_argument("--max-bots", type=int, default=20, help="최대 봇 수")
        parser.add_argument("--step-size", type=int, default=2, help="단계 크기")
        parser.add_argument("--step-duration", type=int, default=30, help="단계 지속시간(초)")
        parser.add_argument("--output", help="결과 저장 파일명")
        parser.add_argument("--interactive", action="store_true", help="대화형 모드 강제 실행")
        
        args = parser.parse_args()
        
        # 시그널 핸들러 등록
        signal.signal(signal.SIGINT, self.signal_handler)
        
        # 테스터 생성
        self.tester = ProgressiveLoadTester(args.host, args.port)
        self.tester.add_step_callback(self.step_callback)
        self.tester.add_failure_callback(self.failure_callback)
        
        # 실행 모드 결정
        if args.scenario or (args.start_bots and not args.interactive):
            # 배치 모드
            return self.run_batch_mode(args)
        else:
            # 대화형 모드
            self.run_interactive_mode(self.tester)
            return 0


if __name__ == "__main__":
    runner = ProgressiveTestRunner()
    sys.exit(runner.main())
