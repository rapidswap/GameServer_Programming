#!/usr/bin/env python3
"""
100개 봇 동시 접속 테스트 스크립트
"""

import time
import signal
import sys
import threading
from datetime import datetime
from load_test_manager import LoadTestManager


class Bot100Test:
    """100개 봇 테스트 클래스"""
    
    def __init__(self):
        self.manager = None
        self.test_running = False
        self.setup_signal_handlers()
    
    def setup_signal_handlers(self):
        """시그널 핸들러 설정 (Ctrl+C 처리)"""
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)
    
    def signal_handler(self, signum, frame):
        """시그널 핸들러"""
        print("\n\n중단 신호 감지됨. 테스트를 안전하게 종료합니다...")
        self.stop_test()
        sys.exit(0)
    
    def print_banner(self):
        """테스트 시작 배너 출력"""
        print("="*80)
        print("         🤖 채팅봇 100개 동시 접속 테스트 🤖")
        print("="*80)
        print(f"시작 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("서버: localhost:9200")
        print("봇 수: 100개")
        print("테스트 종료: Ctrl+C")
        print("="*80)
    
    def start_test(self, test_duration: int = 0):
        """100개 봇 테스트 시작"""
        try:
            self.print_banner()
            
            # 로드테스트 매니저 생성
            print("📡 서버 연결 준비 중...")
            self.manager = LoadTestManager(server_host="localhost", server_port=9200)
            
            # 100개 봇 생성
            print("🤖 100개 봇 생성 중...")
            if not self.manager.create_bots(100):
                print("❌ 봇 생성 실패!")
                return False
            
            print("✅ 100개 봇 생성 완료!")
            
            # 테스트 시작
            print("🚀 테스트 시작...")
            if not self.manager.start_test(test_duration):
                print("❌ 테스트 시작 실패!")
                return False
            
            self.test_running = True
            print("✅ 테스트가 시작되었습니다!")
            print("\n📊 실시간 통계가 5초마다 업데이트됩니다...")
            print("💡 테스트 종료: Ctrl+C를 눌러주세요\n")
            
            # 테스트 실행 대기
            self.wait_for_test_completion(test_duration)
            
            return True
            
        except Exception as e:
            print(f"❌ 테스트 실행 중 오류 발생: {e}")
            return False
        finally:
            self.cleanup()
    
    def wait_for_test_completion(self, test_duration: int):
        """테스트 완료 대기"""
        try:
            if test_duration > 0:
                print(f"⏰ {test_duration}초 후 자동 종료됩니다.")
                
                # 매 초마다 남은 시간 표시
                for remaining in range(test_duration, 0, -1):
                    if not self.test_running:
                        break
                    time.sleep(1)
                    
                    # 매 10초마다 진행상황 표시
                    if remaining % 10 == 0:
                        stats = self.manager.get_current_stats()
                        print(f"⏱️  남은시간: {remaining}초, 연결된 봇: {stats['connected_bots']}/100")
                
                if self.test_running:
                    print("\n⏰ 설정된 테스트 시간이 완료되었습니다.")
                    self.stop_test()
            else:
                # 무한 실행 (수동 종료까지)
                print("♾️  무한 테스트 모드 - Ctrl+C로 종료해주세요")
                while self.test_running:
                    time.sleep(1)
                    
        except KeyboardInterrupt:
            print("\n\n⚠️  Ctrl+C 감지됨. 테스트를 종료합니다...")
            self.stop_test()
    
    def stop_test(self):
        """테스트 중지"""
        if self.manager and self.test_running:
            print("\n🛑 테스트 중지 중...")
            self.test_running = False
            self.manager.stop_test()
            print("✅ 테스트가 안전하게 중지되었습니다.")
            
            # 최종 통계 출력
            self.print_final_stats()
    
    def print_final_stats(self):
        """최종 통계 출력"""
        try:
            print("\n" + "="*80)
            print("📊 최종 테스트 결과")
            print("="*80)
            
            stats = self.manager.get_current_stats()
            
            print(f"⏱️  총 테스트 시간: {stats['elapsed_time']:.1f}초")
            print(f"🤖 생성된 봇 수: {stats['total_bots']}개")
            print(f"🔗 최종 연결된 봇: {stats['connected_bots']}개")
            print(f"📤 총 전송 메시지: {stats['messages_sent']}개")
            print(f"📥 총 수신 메시지: {stats['messages_received']}개")
            print(f"❌ 오류 발생 수: {stats['error_count']}회")
            
            if stats['latency']:
                lat = stats['latency']
                print(f"⚡ 평균 응답시간: {lat['avg']:.1f}ms")
                print(f"⚡ 최소 응답시간: {lat['min']}ms")
                print(f"⚡ 최대 응답시간: {lat['max']}ms")
            
            if stats['elapsed_time'] > 0:
                msg_per_sec = stats['messages_sent'] / stats['elapsed_time']
                success_rate = (stats['connected_bots'] / stats['total_bots']) * 100
                print(f"📊 메시지 처리량: {msg_per_sec:.1f} 메시지/초")
                print(f"📊 연결 성공률: {success_rate:.1f}%")
            
            # 통계 파일 저장
            filename = self.manager.export_stats()
            if filename:
                print(f"💾 상세 통계가 '{filename}'에 저장되었습니다.")
            
            print("="*80)
            
        except Exception as e:
            print(f"최종 통계 출력 중 오류: {e}")
    
    def cleanup(self):
        """정리 작업"""
        if self.manager:
            try:
                self.manager.stop_test()
            except:
                pass


def show_usage():
    """사용법 출력"""
    print("사용법:")
    print("  python test_100_bots.py                    # 무한 테스트 (수동 종료)")
    print("  python test_100_bots.py 300                # 300초(5분) 테스트")
    print("  python test_100_bots.py 1800               # 1800초(30분) 테스트")
    print()
    print("옵션:")
    print("  [시간]  테스트 실행 시간 (초단위, 생략시 무한)")
    print()
    print("종료:")
    print("  Ctrl+C  테스트 중지")


def main():
    """메인 함수"""
    test_duration = 0  # 기본값: 무한
    
    # 명령행 인수 처리
    if len(sys.argv) > 1:
        if sys.argv[1] in ['-h', '--help', 'help']:
            show_usage()
            return
        
        try:
            test_duration = int(sys.argv[1])
            if test_duration < 0:
                print("❌ 테스트 시간은 0 이상이어야 합니다.")
                return
        except ValueError:
            print("❌ 잘못된 테스트 시간입니다. 숫자를 입력해주세요.")
            show_usage()
            return
    
    # 테스트 실행
    test = Bot100Test()
    
    try:
        if test_duration > 0:
            print(f"🕐 {test_duration}초 동안 100개 봇 테스트를 시작합니다...")
        else:
            print("♾️  무한 100개 봇 테스트를 시작합니다...")
        
        test.start_test(test_duration)
        
    except Exception as e:
        print(f"❌ 예상치 못한 오류 발생: {e}")
    
    print("\n👋 테스트가 완전히 종료되었습니다. 감사합니다!")


if __name__ == "__main__":
    main()
