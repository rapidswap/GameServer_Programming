#!/usr/bin/env python3
"""
단일 봇 기본 연결 테스트 - 최소 부하 테스트
"""

import time
import signal
import sys
import threading
from datetime import datetime
from load_test_manager import LoadTestManager


class SingleBotTest:
    """단일 봇 테스트 클래스"""
    
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
        print("="*60)
        print("         🔍 단일 봇 기본 연결 테스트 🔍")
        print("="*60)
        print(f"시작 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("서버: localhost:9200")
        print("봇 수: 1개 (최소 부하)")
        print("연결 방식: 즉시 연결")
        print("메시지 간격: 30초 (최소 부하)")
        print("하트비트: 15초마다")
        print("목적: 서버 기본 동작 확인")
        print("="*60)
    
    def start_test(self, test_duration: int = 0):
        """단일 봇 테스트 시작"""
        try:
            self.print_banner()
            
            # 로드테스트 매니저 생성
            print("📡 서버 연결 준비 중...")
            self.manager = LoadTestManager(server_host="localhost", server_port=9200)
            
            # 1개 봇 생성
            print("🤖 1개 봇 생성 중...")
            if not self.manager.create_bots(1):
                print("❌ 봇 생성 실패!")
                return False
            
            print("✅ 1개 봇 생성 완료!")
            
            # 테스트 시작
            print("🚀 단일 봇 테스트 시작...")
            if not self.manager.start_test(test_duration):
                print("❌ 테스트 시작 실패!")
                return False
            
            self.test_running = True
            print("✅ 테스트가 시작되었습니다!")
            print("\n📊 실시간 상태를 10초마다 확인합니다...")
            print("💡 테스트 종료: Ctrl+C를 눌러주세요")
            
            # 연결 확인
            self.check_connection()
            
            # 테스트 실행 대기
            self.wait_for_test_completion(test_duration)
            
            return True
            
        except Exception as e:
            print(f"❌ 테스트 실행 중 오류 발생: {e}")
            return False
        finally:
            self.cleanup()
    
    def check_connection(self):
        """연결 상태 확인"""
        print("\n🔍 봇 연결 상태 확인 중...")
        
        # 최대 10초 대기
        for i in range(10):
            if not self.test_running:
                break
                
            stats = self.manager.get_current_stats()
            connected = stats['connected_bots']
            errors = stats['error_count']
            
            print(f"⏳ 연결 확인: {i+1}/10초 | 연결: {connected}/1 | 오류: {errors}개", end='\r')
            
            if connected >= 1:
                print(f"\n✅ 봇 연결 성공! (연결 시간: {i+1}초)")
                break
                
            time.sleep(1)
        else:
            print(f"\n❌ 봇 연결 실패! 10초 내에 연결되지 않았습니다.")
            stats = self.manager.get_current_stats()
            print(f"   최종 상태: 연결 {stats['connected_bots']}/1, 오류 {stats['error_count']}개")
            return False
        
        print("🎉 기본 연결 테스트 통과!")
        return True
    
    def wait_for_test_completion(self, test_duration: int):
        """테스트 완료 대기"""
        try:
            if test_duration > 0:
                print(f"\n⏰ {test_duration}초 후 자동 종료됩니다.")
                print("📊 10초마다 상태를 확인합니다...\n")
                
                for remaining in range(test_duration, 0, -10):
                    if not self.test_running:
                        break
                        
                    # 10초 대기
                    for i in range(10):
                        if not self.test_running:
                            break
                        time.sleep(1)
                    
                    # 상태 확인
                    stats = self.manager.get_current_stats()
                    elapsed = stats.get('elapsed_time', 0)
                    
                    print(f"📈 상태 확인 (경과: {elapsed:.0f}초, 남은시간: {remaining}초)")
                    print(f"   🔗 연결: {stats['connected_bots']}/1")
                    print(f"   📨 메시지: 전송 {stats['messages_sent']}, 수신 {stats['messages_received']}")
                    
                    if stats['latency']:
                        print(f"   ⚡ 응답시간: {stats['latency']['avg']:.1f}ms")
                    
                    if stats['connected_bots'] == 0:
                        print("   ⚠️  봇 연결이 끊어졌습니다!")
                    else:
                        print("   ✅ 봇 연결 안정적")
                    print()
                
                if self.test_running:
                    print("⏰ 설정된 테스트 시간이 완료되었습니다.")
                    self.stop_test()
            else:
                # 무한 실행
                print("♾️  무한 테스트 모드 - Ctrl+C로 종료해주세요")
                print("📊 10초마다 상태를 확인합니다...\n")
                
                last_check = time.time()
                while self.test_running:
                    time.sleep(1)
                    
                    # 10초마다 상태 확인
                    if time.time() - last_check >= 10:
                        stats = self.manager.get_current_stats()
                        elapsed = stats.get('elapsed_time', 0)
                        
                        print(f"📈 상태 확인 (경과: {elapsed:.0f}초)")
                        print(f"   🔗 연결: {stats['connected_bots']}/1")
                        print(f"   📨 메시지: {stats['messages_sent']}/{stats['messages_received']}")
                        
                        if stats['connected_bots'] == 0:
                            print("   ⚠️  봇 연결이 끊어졌습니다!")
                        else:
                            print("   ✅ 연결 안정적")
                        print()
                        
                        last_check = time.time()
                    
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
            print("\n" + "="*60)
            print("📊 단일 봇 테스트 최종 결과")
            print("="*60)
            
            stats = self.manager.get_current_stats()
            
            print(f"⏱️  총 테스트 시간: {stats['elapsed_time']:.1f}초")
            print(f"🤖 봇 상태: {stats['connected_bots']}/1")
            print(f"📤 전송 메시지: {stats['messages_sent']}개")
            print(f"📥 수신 메시지: {stats['messages_received']}개")
            print(f"❌ 오류 수: {stats['error_count']}회")
            
            # 연결 안정성 평가
            if stats['connected_bots'] == 1 and stats['error_count'] == 0:
                print("🎉 완벽한 단일 봇 테스트!")
                print("✅ 서버 기본 기능 정상 동작")
                print("💡 다음 단계: 10개 봇 테스트 가능")
            elif stats['connected_bots'] == 1:
                print("✅ 봇 연결 성공 (일부 오류 발생)")
                print("💡 서버 기본 기능 동작하나 최적화 권장")
            else:
                print("❌ 봇 연결 실패")
                print("⚠️  서버 기본 기능에 문제가 있습니다")
                print("🔧 서버 설정 및 상태 점검 필요")
            
            if stats['latency']:
                lat = stats['latency']
                print(f"⚡ 응답시간: {lat['avg']:.1f}ms")
                if lat['avg'] < 20:
                    print("   📊 응답성능: 매우 우수")
                elif lat['avg'] < 50:
                    print("   📊 응답성능: 우수")
                else:
                    print("   📊 응답성능: 보통")
            
            # 통계 파일 저장
            filename = self.manager.export_stats()
            if filename:
                print(f"💾 상세 통계: '{filename}'")
            
            print("="*60)
            
        except Exception as e:
            print(f"최종 통계 출력 중 오류: {e}")
    
    def cleanup(self):
        """정리 작업"""
        if self.manager:
            try:
                self.manager.stop_test()
            except:
                pass


def main():
    """메인 함수"""
    test_duration = 0  # 기본값: 무한
    
    # 명령행 인수 처리
    if len(sys.argv) > 1:
        if sys.argv[1] in ['-h', '--help', 'help']:
            print("사용법:")
            print("  python single_bot_test.py           # 무한 테스트")
            print("  python single_bot_test.py 60        # 60초 테스트")
            print("\n목적: 서버 기본 연결 기능 확인")
            return
        
        try:
            test_duration = int(sys.argv[1])
            if test_duration < 0:
                print("❌ 테스트 시간은 0 이상이어야 합니다.")
                return
        except ValueError:
            print("❌ 잘못된 테스트 시간입니다.")
            return
    
    # 테스트 실행
    test = SingleBotTest()
    
    try:
        if test_duration > 0:
            print(f"🕐 {test_duration}초 동안 단일 봇 테스트를 시작합니다...")
        else:
            print("♾️  무한 단일 봇 테스트를 시작합니다...")
        
        print("💡 이 테스트는 서버의 최소 기능을 확인합니다.")
        print()
        
        test.start_test(test_duration)
        
    except Exception as e:
        print(f"❌ 예상치 못한 오류 발생: {e}")
    
    print("\n👋 단일 봇 테스트가 완전히 종료되었습니다!")


if __name__ == "__main__":
    main()
