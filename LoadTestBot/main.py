"""
메인 실행 파일 - 부하테스트 봇 실행 및 제어
"""

import argparse
import time
import signal
import sys
from load_test_manager import LoadTestManager


class LoadTestRunner:
    """부하테스트 실행기"""
    
    def __init__(self):
        self.manager = None
        self.running = True
    
    def signal_handler(self, signum, frame):
        """시그널 핸들러 (Ctrl+C 처리)"""
        print("\n테스트 중지 중...")
        self.running = False
        if self.manager:
            self.manager.stop_test()
        sys.exit(0)
    
    def run_interactive_mode(self, manager: LoadTestManager):
        """대화형 모드 실행"""
        print("\n=== 채팅서버 부하테스트 봇 ===")
        print("사용 가능한 명령어:")
        print("  start <봇수> [테스트시간(초)] - 부하테스트 시작")
        print("  stop                          - 부하테스트 중지")
        print("  stats                         - 현재 통계 표시")
        print("  export [파일명]               - 통계 JSON 파일로 내보내기")
        print("  broadcast <메시지>            - 모든 봇에게 메시지 전송")
        print("  quit                          - 프로그램 종료")
        print()
        
        while self.running:
            try:
                cmd = input("명령어 입력> ").strip().split()
                if not cmd:
                    continue
                
                command = cmd[0].lower()
                
                if command == "start":
                    if len(cmd) < 2:
                        print("사용법: start <봇수> [테스트시간(초)]")
                        continue
                    
                    try:
                        bot_count = int(cmd[1])
                        test_duration = int(cmd[2]) if len(cmd) > 2 else 0
                        
                        if bot_count <= 0:
                            print("봇 수는 1 이상이어야 합니다.")
                            continue
                        
                        if manager.test_running:
                            print("이미 테스트가 실행 중입니다. 먼저 stop 명령으로 중지하세요.")
                            continue
                        
                        print(f"{bot_count}개의 봇으로 테스트 시작...")
                        if test_duration > 0:
                            print(f"테스트 시간: {test_duration}초")
                        
                        manager.create_bots(bot_count)
                        manager.start_test(test_duration)
                        
                    except ValueError:
                        print("올바른 숫자를 입력하세요.")
                
                elif command == "stop":
                    if not manager.test_running:
                        print("실행 중인 테스트가 없습니다.")
                        continue
                    
                    manager.stop_test()
                    print("테스트가 중지되었습니다.")
                
                elif command == "stats":
                    stats = manager.get_current_stats()
                    manager._print_stats(stats)
                
                elif command == "export":
                    filename = cmd[1] if len(cmd) > 1 else None
                    exported_file = manager.export_stats(filename)
                    if exported_file:
                        print(f"통계가 {exported_file}에 저장되었습니다.")
                
                elif command == "broadcast":
                    if len(cmd) < 2:
                        print("사용법: broadcast <메시지>")
                        continue
                    
                    message = " ".join(cmd[1:])
                    sent_count = manager.send_broadcast_message(message)
                    print(f"{sent_count}개의 봇에게 메시지를 전송했습니다.")
                
                elif command == "quit" or command == "exit":
                    if manager.test_running:
                        print("테스트를 먼저 중지합니다...")
                        manager.stop_test()
                    break
                
                else:
                    print(f"알 수 없는 명령어: {command}")
                    
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"명령어 처리 중 오류: {e}")
        
        print("프로그램을 종료합니다.")
    
    def run_batch_mode(self, args):
        """배치 모드 실행"""
        manager = LoadTestManager(args.host, args.port)
        
        print(f"배치 모드: {args.bots}개 봇으로 {args.duration}초간 테스트")
        
        # 봇 생성 및 테스트 시작
        if not manager.create_bots(args.bots):
            print("봇 생성 실패")
            return 1
        
        if not manager.start_test(args.duration):
            print("테스트 시작 실패")
            return 1
        
        # 테스트 완료까지 대기
        try:
            while manager.test_running:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n테스트 중지됨")
            manager.stop_test()
        
        # 최종 통계 출력
        final_stats = manager.get_current_stats()
        print("\n최종 테스트 결과:")
        manager._print_stats(final_stats)
        
        # 결과 저장
        if args.output:
            manager.export_stats(args.output)
        
        return 0
    
    def main(self):
        """메인 함수"""
        parser = argparse.ArgumentParser(description="채팅서버 부하테스트 봇")
        parser.add_argument("--host", default="localhost", help="서버 호스트 (기본값: localhost)")
        parser.add_argument("--port", type=int, default=9200, help="서버 포트 (기본값: 9200)")
        parser.add_argument("--bots", type=int, help="봇 수 (배치모드)")
        parser.add_argument("--duration", type=int, default=60, help="테스트 시간(초) (배치모드, 기본값: 60)")
        parser.add_argument("--output", help="결과 저장 파일명 (배치모드)")
        parser.add_argument("--interactive", action="store_true", help="대화형 모드 강제 실행")
        
        args = parser.parse_args()
        
        # 시그널 핸들러 등록
        signal.signal(signal.SIGINT, self.signal_handler)
        
        # 매니저 생성
        self.manager = LoadTestManager(args.host, args.port)
        
        # 실행 모드 결정
        if args.bots and not args.interactive:
            # 배치 모드
            return self.run_batch_mode(args)
        else:
            # 대화형 모드
            self.run_interactive_mode(self.manager)
            return 0


if __name__ == "__main__":
    runner = LoadTestRunner()
    sys.exit(runner.main())
