#!/usr/bin/env python3
"""
시간 동기화 테스트 스크립트
"""

import time
from windows_time import get_server_timestamp, test_time_compatibility

def main():
    print("🕐 서버 시간 동기화 테스트")
    print("="*50)
    
    # 시간 호환성 테스트
    test_time_compatibility()
    
    print("\n📊 연속 시간 측정 테스트:")
    print("5초 동안 1초마다 측정...")
    
    start_time = get_server_timestamp()
    print(f"시작 시간: {start_time}")
    
    for i in range(5):
        time.sleep(1)
        current_time = get_server_timestamp()
        elapsed = current_time - start_time
        print(f"  {i+1}초 후: {current_time} (경과: {elapsed}ms)")
    
    print("\n✅ 시간 동기화 테스트 완료!")
    print("이제 서버와 봇의 시간이 동기화되어야 합니다.")

if __name__ == "__main__":
    main()
