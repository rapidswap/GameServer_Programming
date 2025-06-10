"""
Windows 시스템 시간 유틸리티 - GetTickCount64() 호환
"""

import time
import ctypes
from ctypes import wintypes
import logging


class WindowsTimeUtil:
    """Windows 시스템 시간 유틸리티"""
    
    _kernel32 = None
    _GetTickCount64 = None
    _initialized = False
    
    @classmethod
    def _initialize(cls):
        """Windows API 초기화"""
        if cls._initialized:
            return
            
        try:
            cls._kernel32 = ctypes.windll.kernel32
            cls._GetTickCount64 = cls._kernel32.GetTickCount64
            cls._GetTickCount64.restype = wintypes.ULARGE_INTEGER
            cls._initialized = True
            logging.info("Windows GetTickCount64 API initialized successfully")
        except Exception as e:
            logging.warning(f"Failed to initialize Windows API: {e}")
            cls._initialized = False
    
    @classmethod
    def get_tick_count(cls) -> int:
        """
        Windows GetTickCount64()와 호환되는 시간 반환
        시스템 부팅 후 경과 시간을 밀리초로 반환
        """
        cls._initialize()
        
        if cls._initialized and cls._GetTickCount64:
            try:
                return cls._GetTickCount64()
            except Exception as e:
                logging.warning(f"GetTickCount64 call failed: {e}")
        
        # Fallback: time.perf_counter() 사용 (상대적 시간)
        # 정확하지 않지만 Windows API 실패 시 대안
        return int(time.perf_counter() * 1000)
    
    @classmethod
    def get_timestamp_ms(cls) -> int:
        """
        서버 호환 타임스탬프 반환 (밀리초)
        """
        return cls.get_tick_count()


# 전역 함수로 쉽게 사용
def get_server_timestamp() -> int:
    """서버와 호환되는 타임스탬프 반환"""
    return WindowsTimeUtil.get_timestamp_ms()


def get_current_time_ms() -> int:
    """현재 시간을 밀리초로 반환 (서버 호환)"""
    return WindowsTimeUtil.get_tick_count()


# 테스트 함수
def test_time_compatibility():
    """시간 호환성 테스트"""
    print("Windows 시간 호환성 테스트:")
    
    # 기존 방식
    old_time = int(time.time() * 1000)
    
    # 새로운 방식 (서버 호환)
    new_time = get_server_timestamp()
    
    print(f"기존 time.time() * 1000: {old_time}")
    print(f"새로운 GetTickCount64(): {new_time}")
    print(f"차이: {abs(old_time - new_time)} ms")
    
    # 연속 측정으로 안정성 확인
    times = []
    for i in range(5):
        times.append(get_server_timestamp())
        time.sleep(0.1)
    
    print("연속 측정 결과 (100ms 간격):")
    for i in range(1, len(times)):
        diff = times[i] - times[i-1]
        print(f"  측정 {i}: {diff}ms 경과")


if __name__ == "__main__":
    test_time_compatibility()
