#!/usr/bin/env python3
"""
빠른 100개 봇 지속 대화 - 간단 실행
"""

import time
import signal
import sys
from datetime import datetime
from load_test_manager import LoadTestManager


def signal_handler(signum, frame):
    """Ctrl+C 핸들러"""
    print("\n\n⚠️  100개 봇 대화 종료 중...")
    sys.exit(0)


def main():
    """빠른 100개 봇 대화"""
    # Ctrl+C 핸들러 설정
    signal.signal(signal.SIGINT, signal_handler)
    
    print("🤖💬 100개 봇 빠른 지속 대화!")
    print(f"📅 시작: {datetime.now().strftime('%H:%M:%S')}")
    print("🛑 종료: Ctrl+C")
    print("-" * 50)
    
    try:
        # 매니저 생성 및 봇 생성
        print("📡 100개 봇 준비 중...")
        manager = LoadTestManager("localhost", 9200)
        manager.create_bots(100)
        
        # 무한 테스트 시작
        print("🚀 지속 대화 시작!")
        manager.start_test(0)  # 무한
        
        # 연결 대기
        time.sleep(30)
        print("💬 대화 진행 중...")
        
        # 무한 루프 (상태 출력)
        last_update = time.time()
        while True:
            if time.time() - last_update >= 60:  # 1분마다
                stats = manager.get_current_stats()
                elapsed = stats.get('elapsed_time', 0)
                print(f"⏰ {datetime.now().strftime('%H:%M:%S')} | "
                      f"경과: {elapsed/60:.0f}분 | "
                      f"연결: {stats['connected_bots']}/100 | "
                      f"대화: {stats['messages_sent']}")
                last_update = time.time()
            time.sleep(5)
            
    except KeyboardInterrupt:
        print("\n✅ 100개 봇 대화 완료!")
    except Exception as e:
        print(f"❌ 오류: {e}")


if __name__ == "__main__":
    main()
