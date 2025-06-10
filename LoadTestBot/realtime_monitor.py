#!/usr/bin/env python3
"""
실시간 서버 성능 모니터링
"""

import psutil
import time
import signal
import sys
from datetime import datetime


class ServerMonitor:
    """서버 성능 모니터"""
    
    def __init__(self):
        self.running = False
        self.setup_signal_handlers()
    
    def setup_signal_handlers(self):
        """시그널 핸들러 설정"""
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)
    
    def signal_handler(self, signum, frame):
        """시그널 핸들러"""
        print("\n\n모니터링을 종료합니다...")
        self.running = False
        sys.exit(0)
    
    def find_server_process(self):
        """채팅서버 프로세스 찾기"""
        for proc in psutil.process_iter(['pid', 'name', 'exe']):
            try:
                if 'ChattingServer' in proc.info['name'] or 'ChattingServer' in str(proc.info['exe']):
                    return psutil.Process(proc.info['pid'])
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        return None
    
    def get_network_connections(self, port=9200):
        """특정 포트의 네트워크 연결 수 확인"""
        connections = 0
        try:
            for conn in psutil.net_connections():
                if conn.laddr.port == port and conn.status == 'ESTABLISHED':
                    connections += 1
        except (psutil.AccessDenied, AttributeError):
            pass
        return connections
    
    def format_bytes(self, bytes_val):
        """바이트를 읽기 쉬운 형태로 변환"""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if bytes_val < 1024.0:
                return f"{bytes_val:.1f}{unit}"
            bytes_val /= 1024.0
        return f"{bytes_val:.1f}TB"
    
    def start_monitoring(self, interval=5):
        """모니터링 시작"""
        self.running = True
        
        print("="*80)
        print("🖥️  실시간 서버 성능 모니터링")
        print("="*80)
        print("포트 9200 모니터링 중...")
        print("종료: Ctrl+C")
        print("="*80)
        
        while self.running:
            try:
                # 현재 시간
                current_time = datetime.now().strftime('%H:%M:%S')
                
                # 서버 프로세스 찾기
                server_proc = self.find_server_process()
                
                # 시스템 전체 정보
                cpu_percent = psutil.cpu_percent(interval=1)
                memory = psutil.virtual_memory()
                
                # 네트워크 연결 수
                connections = self.get_network_connections(9200)
                
                # 출력 헤더
                print(f"\n⏰ {current_time} | 연결수: {connections:3d} | "
                      f"시스템 CPU: {cpu_percent:5.1f}% | "
                      f"메모리: {memory.percent:5.1f}%")
                
                if server_proc:
                    try:
                        # 서버 프로세스 정보
                        proc_cpu = server_proc.cpu_percent()
                        proc_memory = server_proc.memory_info()
                        proc_threads = server_proc.num_threads()
                        
                        print(f"🖥️  서버 프로세스 [PID:{server_proc.pid}]")
                        print(f"   CPU: {proc_cpu:5.1f}% | "
                              f"메모리: {self.format_bytes(proc_memory.rss)} | "
                              f"스레드: {proc_threads}")
                        
                        # 위험 수준 경고
                        if proc_cpu > 80:
                            print("⚠️  경고: 서버 CPU 사용률 80% 초과!")
                        if memory.percent > 85:
                            print("⚠️  경고: 시스템 메모리 사용률 85% 초과!")
                        if connections > 90:
                            print("⚠️  경고: 연결 수가 90개를 초과했습니다!")
                            
                    except (psutil.NoSuchProcess, psutil.AccessDenied):
                        print("❌ 서버 프로세스 정보 접근 실패")
                else:
                    print("❌ 채팅서버 프로세스를 찾을 수 없습니다.")
                
                # 시스템 리소스 상태
                if cpu_percent > 90:
                    print("🔥 시스템 CPU 과부하!")
                elif cpu_percent > 70:
                    print("⚡ 시스템 CPU 높음")
                
                if memory.percent > 90:
                    print("🔥 시스템 메모리 부족!")
                elif memory.percent > 80:
                    print("⚡ 시스템 메모리 높음")
                
                print("-" * 60)
                
                time.sleep(interval)
                
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"모니터링 오류: {e}")
                time.sleep(interval)
        
        print("\n모니터링이 종료되었습니다.")


def main():
    """메인 함수"""
    monitor = ServerMonitor()
    
    print("서버 성능 모니터링을 시작합니다...")
    print("💡 별도 터미널에서 봇 테스트를 실행하세요.")
    
    try:
        monitor.start_monitoring(interval=3)  # 3초마다 업데이트
    except Exception as e:
        print(f"모니터링 실행 오류: {e}")


if __name__ == "__main__":
    main()
