#!/usr/bin/env python3
"""
간단한 100개 봇 테스트 - 바로 실행
"""

import time
import signal
import sys
from datetime import datetime
from load_test_manager import LoadTestManager


def signal_handler(signum, frame):
    """Ctrl+C 핸들러"""
    print("\n\n⚠️  테스트 중지 중...")
    sys.exit(0)


def main():
    """간단한 100개 봇 테스트"""
    # Ctrl+C 핸들러 설정
    signal.signal(signal.SIGINT, signal_handler)
    
    print("🤖 100개 봇 빠른 테스트 시작!")
    print(f"📅 시작시간: {datetime.now().strftime('%H:%M:%S')}")
    print("🛑 중지: Ctrl+C")
    print("-" * 50)
    
    try:
        # 매니저 생성 및 봇 생성
        manager = LoadTestManager("localhost", 9200)
        manager.create_bots(100)
        
        # 테스트 시작
        manager.start_test()
        
        # 연결 완료까지 대기
        print("📡 봇들이 연결 중입니다...")
        time.sleep(10)  # 10초 대기
        
        # 무한 루프 (Ctrl+C까지)
        while True:
            stats = manager.get_current_stats()
            print(f"⏰ {datetime.now().strftime('%H:%M:%S')} | "
                  f"연결: {stats['connected_bots']}/100 | "
                  f"전송: {stats['messages_sent']} | "
                  f"수신: {stats['messages_received']}")
            time.sleep(10)  # 10초마다 상태 출력
            
    except KeyboardInterrupt:
        print("\n✅ 테스트 완료!")
    except Exception as e:
        print(f"❌ 오류: {e}")


if __name__ == "__main__":
    main()
