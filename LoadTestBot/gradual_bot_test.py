#!/usr/bin/env python3
"""
점진적 봇 증가 테스트 - 서버 한계점 탐지
"""

import time
import signal
import sys
import threading
from datetime import datetime
from load_test_manager import LoadTestManager


class GradualBotTest:
    """점진적 봇 증가 테스트 클래스"""
    
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
        print("         📈 점진적 봇 증가 테스트 (서버 한계점 탐지) 📈")
        print("="*80)
        print(f"시작 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("서버: localhost:9200")
        print("테스트 단계: 10 → 20 → 30 → 50 → 70 → 100개")
        print("각 단계: 60초간 안정성 테스트")
        print("연결 실패 시: 이전 단계로 복귀")
        print("테스트 종료: Ctrl+C")
        print("="*80)
    
    def start_test(self):
        """점진적 테스트 시작"""
        try:
            self.print_banner()
            self.test_running = True
            
            # 테스트 단계 정의
            test_stages = [10, 20, 30, 50, 70, 100]
            max_stable_bots = 0
            
            for stage_bots in test_stages:
                if not self.test_running:
                    break
                
                print(f"\n🚀 단계 {stage_bots}: {stage_bots}개 봇 테스트 시작")
                print("-" * 50)
                
                # 새로운 매니저 생성
                self.manager = LoadTestManager(server_host="localhost", server_port=9200)
                
                # 봇 생성
                if not self.manager.create_bots(stage_bots):
                    print(f"❌ {stage_bots}개 봇 생성 실패!")
                    break
                
                # 테스트 시작
                if not self.manager.start_test(60):  # 60초간
                    print(f"❌ {stage_bots}개 봇 테스트 시작 실패!")
                    break
                
                # 연결 완료 대기 (최대 30초)
                success = self.wait_for_connections(stage_bots, timeout=30)
                
                if success:
                    print(f"✅ {stage_bots}개 봇 연결 성공!")
                    max_stable_bots = stage_bots
                    
                    # 60초간 안정성 테스트
                    print(f"⏰ {stage_bots}개 봇으로 60초간 안정성 테스트...")
                    self.stability_test(60)
                    
                    # 연결 상태 최종 확인
                    final_stats = self.manager.get_current_stats()
                    final_connected = final_stats['connected_bots']
                    
                    if final_connected >= stage_bots * 0.9:  # 90% 이상 유지
                        print(f"🎉 {stage_bots}개 봇 안정성 테스트 통과!")
                        print(f"   최종 연결: {final_connected}/{stage_bots}")
                    else:
                        print(f"⚠️  {stage_bots}개 봇 안정성 테스트 실패")
                        print(f"   최종 연결: {final_connected}/{stage_bots}")
                        max_stable_bots = max(max_stable_bots - 10, 0)  # 이전 단계로
                        break
                else:
                    print(f"❌ {stage_bots}개 봇 연결 실패!")
                    print(f"💡 서버 한계점: {max_stable_bots}개 봇")
                    break
                
                # 다음 단계 전 정리
                self.cleanup_current_test()
                
                if not self.test_running:
                    break
                
                # 다음 단계 전 잠깐 대기
                print("⏳ 다음 단계 준비 중... (5초 대기)")
                time.sleep(5)
            
            # 최종 결과 출력
            self.print_final_results(max_stable_bots, test_stages)
            
            return True
            
        except Exception as e:
            print(f"❌ 테스트 실행 중 오류 발생: {e}")
            return False
        finally:
            self.cleanup()
    
    def wait_for_connections(self, target_bots: int, timeout: int = 30) -> bool:
        """연결 완료 대기"""
        print(f"📶 {target_bots}개 봇 연결 대기 중... (최대 {timeout}초)")
        
        start_time = time.time()
        while time.time() - start_time < timeout:
            if not self.test_running:
                return False
                
            stats = self.manager.get_current_stats()
            connected = stats['connected_bots']
            errors = stats['error_count']
            
            progress = (connected / target_bots) * 100 if target_bots > 0 else 0
            
            print(f"🔗 연결 진행: {connected}/{target_bots} ({progress:.1f}%) | 오류: {errors}개", end='\r')
            
            # 80% 이상 연결되면 성공으로 간주
            if connected >= target_bots * 0.8:
                print(f"\n✅ 연결 완료! {connected}/{target_bots} 봇 연결됨")
                return True
                
            # 오류가 너무 많으면 실패
            if errors > target_bots * 0.3:
                print(f"\n❌ 연결 오류 과다: {errors}개")
                return False
            
            time.sleep(1)
        
        print(f"\n⏰ 연결 시간 초과")
        return False
    
    def stability_test(self, duration: int):
        """안정성 테스트"""
        start_time = time.time()
        
        while time.time() - start_time < duration:
            if not self.test_running:
                break
                
            stats = self.manager.get_current_stats()
            remaining = int(duration - (time.time() - start_time))
            
            print(f"⏱️  안정성 테스트: {remaining}초 남음 | "
                  f"연결: {stats['connected_bots']} | "
                  f"메시지: {stats['messages_sent']}/{stats['messages_received']}", 
                  end='\r')
            
            time.sleep(5)  # 5초마다 상태 확인
        
        print()  # 줄바꿈
    
    def cleanup_current_test(self):
        """현재 테스트 정리"""
        if self.manager:
            try:
                self.manager.stop_test()
                time.sleep(2)  # 정리 시간
            except:
                pass
    
    def print_final_results(self, max_stable_bots: int, test_stages: list):
        """최종 결과 출력"""
        print("\n" + "="*80)
        print("📊 점진적 테스트 최종 결과")
        print("="*80)
        
        print(f"🏆 최대 안정 봇 수: {max_stable_bots}개")
        
        if max_stable_bots >= 100:
            print("🎉 100개 봇 완전 성공! 서버 성능 우수!")
        elif max_stable_bots >= 70:
            print("✅ 70개 이상 안정 - 서버 성능 양호")
        elif max_stable_bots >= 50:
            print("⚠️  50개 이상 안정 - 서버 최적화 필요")
        else:
            print("❌ 50개 미만 - 서버 성능 개선 필요")
        
        print(f"\n📈 테스트 진행 상황:")
        for stage in test_stages:
            if stage <= max_stable_bots:
                print(f"   {stage:3d}개 봇: ✅ 성공")
            else:
                print(f"   {stage:3d}개 봇: ❌ 실패")
        
        print(f"\n💡 추천사항:")
        if max_stable_bots < 50:
            print("   • 서버 하드웨어 업그레이드 필요")
            print("   • 코드 최적화 검토")
        elif max_stable_bots < 100:
            print("   • 스레드 풀 크기 조정")
            print("   • 메모리 사용량 최적화")
        else:
            print("   • 서버 성능 우수!")
            print("   • 더 많은 봇으로 테스트 가능")
        
        print("="*80)
    
    def stop_test(self):
        """테스트 중지"""
        self.test_running = False
        if self.manager:
            try:
                self.manager.stop_test()
            except:
                pass
    
    def cleanup(self):
        """정리 작업"""
        self.stop_test()


def main():
    """메인 함수"""
    print("🧪 점진적 봇 증가 테스트를 시작합니다...")
    print("💡 이 테스트는 서버의 안전한 최대 동접자 수를 찾습니다.")
    print()
    
    # 확인 메시지
    confirm = input("테스트를 시작하시겠습니까? (y/n): ")
    if confirm.lower() != 'y':
        print("테스트를 취소했습니다.")
        return
    
    # 테스트 실행
    test = GradualBotTest()
    
    try:
        test.start_test()
    except Exception as e:
        print(f"❌ 예상치 못한 오류 발생: {e}")
    
    print("\n👋 점진적 테스트가 완전히 종료되었습니다.")


if __name__ == "__main__":
    main()
