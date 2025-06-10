#!/usr/bin/env python3
"""
안전한 10개 봇 테스트 - 기본 안정성 확인
"""

import time
import signal
import sys
import threading
from datetime import datetime
from load_test_manager import LoadTestManager


class Safe10BotTest:
    """안전한 10개 봇 테스트 클래스"""
    
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
        print("="*70)
        print("         🛡️ 안전한 10개 봇 기본 테스트 🛡️")
        print("="*70)
        print(f"시작 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("서버: localhost:9200")
        print("봇 수: 10개 (2개씩 배치 연결)")
        print("연결 간격: 봇 간 1초, 배치 간 3초")
        print("메시지 간격: 15-25초 (서버 부하 최소화)")
        print("하트비트: 10초마다")
        print("핑 테스트: 비활성화")
        print("테스트 종료: Ctrl+C")
        print("="*70)
    
    def start_test(self, test_duration: int = 0):
        """안전한 10개 봇 테스트 시작"""
        try:
            self.print_banner()
            
            # 로드테스트 매니저 생성
            print("📡 서버 연결 준비 중...")
            self.manager = LoadTestManager(server_host="localhost", server_port=9200)
            
            # 10개 봇 생성
            print("🤖 10개 봇 생성 중...")
            if not self.manager.create_bots(10):
                print("❌ 봇 생성 실패!")
                return False
            
            print("✅ 10개 봇 생성 완료!")
            print("📋 연결 방식: 2개씩 배치로 매우 안전하게 연결")
            print("⏰ 예상 연결 시간: 약 15초")
            
            # 테스트 시작
            print("🚀 매우 안전한 테스트 시작...")
            if not self.manager.start_test(test_duration):
                print("❌ 테스트 시작 실패!")
                return False
            
            self.test_running = True
            print("✅ 테스트가 시작되었습니다!")
            print("\n📊 실시간 통계가 5초마다 업데이트됩니다...")
            print("💡 테스트 종료: Ctrl+C를 눌러주세요")
            print("\n🔍 연결 진행 상황:")
            
            # 연결 진행 상황 모니터링
            self.monitor_connection_progress()
            
            # 테스트 실행 대기
            self.wait_for_test_completion(test_duration)
            
            return True
            
        except Exception as e:
            print(f"❌ 테스트 실행 중 오류 발생: {e}")
            return False
        finally:
            self.cleanup()
    
    def monitor_connection_progress(self):
        """연결 진행 상황 모니터링"""
        print("📶 봇 연결 진행 상황 모니터링 시작...")
        
        # 처음 20초 동안 연결 상황 모니터링
        for i in range(20):
            if not self.test_running:
                break
                
            stats = self.manager.get_current_stats()
            connected = stats['connected_bots']
            total = stats['total_bots']
            errors = stats['error_count']
            
            progress = (connected / total) * 100 if total > 0 else 0
            
            print(f"🔗 연결 진행: {connected}/{total} ({progress:.1f}%) | 오류: {errors}개", end='\r')
            
            # 모든 봇이 연결되면 종료
            if connected >= total:
                print(f"\n🎉 완벽한 연결! {connected}/{total} 봇이 모두 연결되었습니다!")
                break
            
            # 80% 이상 연결되면 성공으로 간주
            if connected >= total * 0.8:
                print(f"\n✅ 연결 성공! {connected}/{total} 봇이 연결되었습니다.")
                break
                
            time.sleep(1)
        
        if self.test_running:
            print(f"\n📊 최종 연결 결과:")
            stats = self.manager.get_current_stats()
            success_rate = (stats['connected_bots']/stats['total_bots']*100)
            
            print(f"   성공: {stats['connected_bots']}/{stats['total_bots']} 봇")
            print(f"   실패: {stats['error_count']}개")
            print(f"   성공률: {success_rate:.1f}%")
            
            if success_rate >= 80:
                print("✅ 기본 연결 테스트 통과!")
                print("🏃‍♂️ 안정성 테스트를 시작합니다...")
            else:
                print("⚠️  연결 성공률이 낮습니다. 서버 상태를 확인해주세요.")
    
    def wait_for_test_completion(self, test_duration: int):
        """테스트 완료 대기"""
        try:
            if test_duration > 0:
                print(f"\n⏰ {test_duration}초 후 자동 종료됩니다.")
                
                # 매 10초마다 상태 요약 표시
                for remaining in range(test_duration, 0, -10):
                    if not self.test_running:
                        break
                        
                    for i in range(10):
                        if not self.test_running:
                            break
                        time.sleep(1)
                    
                    # 10초마다 간단한 상태 표시
                    if remaining % 20 == 0:  # 20초마다 상세 정보
                        stats = self.manager.get_current_stats()
                        print(f"\n⏱️  남은시간: {remaining}초")
                        print(f"   🔗 연결상태: {stats['connected_bots']}/10")
                        print(f"   📨 메시지: 전송 {stats['messages_sent']}, 수신 {stats['messages_received']}")
                        if stats['latency']:
                            print(f"   ⚡ 응답시간: {stats['latency']['avg']:.1f}ms")
                        
                        # 연결 상태 체크
                        if stats['connected_bots'] < 5:
                            print("   ⚠️  연결된 봇이 절반 이하로 줄었습니다!")
                
                if self.test_running:
                    print("\n⏰ 설정된 테스트 시간이 완료되었습니다.")
                    self.stop_test()
            else:
                # 무한 실행 (수동 종료까지)
                print("♾️  무한 테스트 모드 - Ctrl+C로 종료해주세요")
                last_status_time = time.time()
                
                while self.test_running:
                    time.sleep(1)
                    
                    # 10초마다 간단한 상태 출력
                    if time.time() - last_status_time >= 10:
                        stats = self.manager.get_current_stats()
                        elapsed = stats.get('elapsed_time', 0)
                        print(f"\n📊 상태 업데이트 (경과: {elapsed:.0f}초)")
                        print(f"   🔗 연결: {stats['connected_bots']}/10")
                        print(f"   📨 메시지: {stats['messages_sent']}/{stats['messages_received']}")
                        if stats['connected_bots'] < 5:
                            print("   ⚠️  연결 상태 불안정!")
                        last_status_time = time.time()
                    
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
            print("\n" + "="*70)
            print("📊 최종 10개 봇 테스트 결과")
            print("="*70)
            
            stats = self.manager.get_current_stats()
            
            print(f"⏱️  총 테스트 시간: {stats['elapsed_time']:.1f}초")
            print(f"🤖 생성된 봇 수: {stats['total_bots']}개")
            print(f"🔗 최종 연결된 봇: {stats['connected_bots']}개")
            print(f"📤 총 전송 메시지: {stats['messages_sent']}개")
            print(f"📥 총 수신 메시지: {stats['messages_received']}개")
            print(f"❌ 연결 오류 수: {stats['error_count']}회")
            
            # 성공률 계산
            success_rate = (stats['connected_bots'] / stats['total_bots']) * 100
            if success_rate >= 90:
                print(f"🎉 연결 성공률: {success_rate:.1f}% (우수)")
                print("✅ 서버 기본 안정성 확인!")
            elif success_rate >= 70:
                print(f"✅ 연결 성공률: {success_rate:.1f}% (양호)")
                print("💡 서버 상태 괜찮음")
            else:
                print(f"⚠️  연결 성공률: {success_rate:.1f}% (문제 있음)")
                print("❌ 서버 최적화 필요")
            
            if stats['latency']:
                lat = stats['latency']
                print(f"⚡ 평균 응답시간: {lat['avg']:.1f}ms")
                if lat['avg'] < 30:
                    print("   📊 응답시간: 매우 우수")
                elif lat['avg'] < 50:
                    print("   📊 응답시간: 우수")
                elif lat['avg'] < 100:
                    print("   📊 응답시간: 양호")
                else:
                    print("   📊 응답시간: 개선 필요")
            
            if stats['elapsed_time'] > 0:
                msg_per_sec = stats['messages_sent'] / stats['elapsed_time']
                print(f"📊 메시지 처리량: {msg_per_sec:.2f} 메시지/초")
            
            # 통계 파일 저장
            filename = self.manager.export_stats()
            if filename:
                print(f"💾 상세 통계가 '{filename}'에 저장되었습니다.")
            
            # 추천사항
            print("\n💡 분석 결과:")
            if success_rate >= 90 and stats['latency'] and stats['latency']['avg'] < 50:
                print("   🎯 10개 봇 테스트 완벽 통과!")
                print("   🚀 더 많은 봇으로 테스트 가능")
                print("   📈 점진적 증가 테스트 권장 (20개 → 30개)")
            elif success_rate >= 70:
                print("   ✅ 기본 안정성 확인됨")
                print("   💡 서버 최적화 후 봇 수 증가 고려")
            else:
                print("   ⚠️  서버 안정성 문제 감지")
                print("   🔧 서버 설정 및 리소스 점검 필요")
                print("   📊 단일 봇 테스트부터 재시작 권장")
            
            print("="*70)
            
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
    print("  python safe_10_test.py                     # 무한 테스트 (수동 종료)")
    print("  python safe_10_test.py 120                 # 120초(2분) 테스트")
    print("  python safe_10_test.py 300                 # 300초(5분) 테스트")
    print()
    print("특징:")
    print("  • 2개씩 배치로 매우 안전한 연결")
    print("  • 서버 부하 최소화")
    print("  • 기본 안정성 확인")
    print("  • 상세한 성능 분석")
    print()
    print("목적:")
    print("  • 서버 기본 동작 확인")
    print("  • 최소 부하에서의 안정성 테스트")
    print("  • 추가 테스트 가능성 판단")


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
    test = Safe10BotTest()
    
    try:
        if test_duration > 0:
            print(f"🕐 {test_duration}초 동안 안전한 10개 봇 테스트를 시작합니다...")
        else:
            print("♾️  무한 안전 10개 봇 테스트를 시작합니다...")
        
        print("💡 이 테스트는 서버의 기본 안정성을 확인합니다.")
        print()
        
        test.start_test(test_duration)
        
    except Exception as e:
        print(f"❌ 예상치 못한 오류 발생: {e}")
    
    print("\n👋 안전한 10개 봇 테스트가 완전히 종료되었습니다!")


if __name__ == "__main__":
    main()
