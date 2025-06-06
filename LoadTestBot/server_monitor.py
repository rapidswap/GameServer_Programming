"""
서버 모니터링 도구 - 서버 성능 및 리소스 모니터링
"""

import psutil
import time
import json
import logging
import threading
import socket
from datetime import datetime
from typing import Dict, List, Optional


class ServerMonitor:
    """서버 모니터링 클래스"""
    
    def __init__(self, process_name: str = "ChattingServer.exe", update_interval: float = 1.0):
        self.process_name = process_name
        self.update_interval = update_interval
        self.monitoring = False
        
        # 모니터링 데이터
        self.server_process: Optional[psutil.Process] = None
        self.monitoring_data: List[Dict] = []
        self.start_time: Optional[float] = None
        
        # 스레드
        self.monitor_thread: Optional[threading.Thread] = None
        
        # 로깅
        self.logger = logging.getLogger("ServerMonitor")
        logging.basicConfig(level=logging.INFO)
    
    def find_server_process(self) -> bool:
        """서버 프로세스 찾기"""
        try:
            for proc in psutil.process_iter(['pid', 'name', 'exe']):
                if self.process_name.lower() in proc.info['name'].lower():
                    self.server_process = psutil.Process(proc.info['pid'])
                    self.logger.info(f"Server process found: PID {proc.info['pid']}")
                    return True
            
            self.logger.warning(f"Server process '{self.process_name}' not found")
            return False
            
        except Exception as e:
            self.logger.error(f"Error finding server process: {e}")
            return False
    
    def start_monitoring(self):
        """모니터링 시작"""
        if self.monitoring:
            self.logger.warning("Monitoring already started")
            return False
        
        if not self.find_server_process():
            return False
        
        self.monitoring = True
        self.start_time = time.time()
        self.monitoring_data = []
        
        self.monitor_thread = threading.Thread(target=self._monitoring_loop, daemon=True)
        self.monitor_thread.start()
        
        self.logger.info("Server monitoring started")
        return True
    
    def stop_monitoring(self):
        """모니터링 중지"""
        self.monitoring = False
        if self.monitor_thread:
            self.monitor_thread.join(timeout=2.0)
        
        self.logger.info("Server monitoring stopped")
    
    def _monitoring_loop(self):
        """모니터링 루프"""
        while self.monitoring:
            try:
                data = self._collect_system_metrics()
                if data:
                    self.monitoring_data.append(data)
                    self._print_current_stats(data)
                
                time.sleep(self.update_interval)
                
            except Exception as e:
                self.logger.error(f"Monitoring loop error: {e}")
                if not self._check_process_alive():
                    self.logger.warning("Server process no longer exists")
                    break
    
    def _collect_system_metrics(self) -> Optional[Dict]:
        """시스템 메트릭 수집"""
        try:
            timestamp = time.time()
            
            # 전체 시스템 메트릭
            cpu_percent = psutil.cpu_percent(interval=None)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')
            
            # 네트워크 메트릭
            net_io = psutil.net_io_counters()
            
            # 서버 프로세스 메트릭
            process_metrics = {}
            if self.server_process and self._check_process_alive():
                try:
                    process_metrics = {
                        'cpu_percent': self.server_process.cpu_percent(),
                        'memory_info': self.server_process.memory_info()._asdict(),
                        'memory_percent': self.server_process.memory_percent(),
                        'num_threads': self.server_process.num_threads(),
                        'num_fds': self.server_process.num_fds() if hasattr(self.server_process, 'num_fds') else 0,
                        'connections': len(self.server_process.connections()),
                        'status': self.server_process.status()
                    }
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    self.logger.warning("Lost access to server process")
                    return None
            
            return {
                'timestamp': timestamp,
                'datetime': datetime.fromtimestamp(timestamp).isoformat(),
                'system': {
                    'cpu_percent': cpu_percent,
                    'memory': {
                        'total': memory.total,
                        'available': memory.available,
                        'used': memory.used,
                        'percent': memory.percent
                    },
                    'disk': {
                        'total': disk.total,
                        'used': disk.used,
                        'free': disk.free,
                        'percent': disk.percent
                    },
                    'network': {
                        'bytes_sent': net_io.bytes_sent,
                        'bytes_recv': net_io.bytes_recv,
                        'packets_sent': net_io.packets_sent,
                        'packets_recv': net_io.packets_recv
                    }
                },
                'process': process_metrics
            }
            
        except Exception as e:
            self.logger.error(f"Error collecting metrics: {e}")
            return None
    
    def _check_process_alive(self) -> bool:
        """프로세스 생존 확인"""
        if not self.server_process:
            return False
        
        try:
            return self.server_process.is_running()
        except:
            return False
    
    def _print_current_stats(self, data: Dict):
        """현재 통계 출력"""
        if not data:
            return
        
        elapsed = time.time() - self.start_time if self.start_time else 0
        
        print(f"\n서버 모니터링 - {data['datetime']} (경과: {elapsed:.1f}초)")
        print("=" * 70)
        
        # 시스템 메트릭
        sys_data = data['system']
        print(f"시스템 CPU: {sys_data['cpu_percent']:.1f}%")
        print(f"시스템 메모리: {sys_data['memory']['percent']:.1f}% "
              f"({self._format_bytes(sys_data['memory']['used'])}/{self._format_bytes(sys_data['memory']['total'])})")
        print(f"디스크 사용량: {sys_data['disk']['percent']:.1f}% "
              f"({self._format_bytes(sys_data['disk']['used'])}/{self._format_bytes(sys_data['disk']['total'])})")
        
        # 네트워크
        net_data = sys_data['network']
        print(f"네트워크: 송신 {self._format_bytes(net_data['bytes_sent'])}, "
              f"수신 {self._format_bytes(net_data['bytes_recv'])}")
        
        # 프로세스 메트릭
        if data['process']:
            proc_data = data['process']
            print(f"\n서버 프로세스:")
            print(f"  CPU: {proc_data['cpu_percent']:.1f}%")
            print(f"  메모리: {proc_data['memory_percent']:.1f}% "
                  f"({self._format_bytes(proc_data['memory_info']['rss'])})")
            print(f"  스레드: {proc_data['num_threads']}")
            print(f"  연결: {proc_data['connections']}")
            print(f"  상태: {proc_data['status']}")
        else:
            print("\n서버 프로세스: 찾을 수 없음")
    
    def _format_bytes(self, bytes_value: int) -> str:
        """바이트를 읽기 좋은 형태로 변환"""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if bytes_value < 1024.0:
                return f"{bytes_value:.1f}{unit}"
            bytes_value /= 1024.0
        return f"{bytes_value:.1f}PB"
    
    def get_summary_stats(self) -> Dict:
        """요약 통계 반환"""
        if not self.monitoring_data:
            return {}
        
        # CPU 사용률 통계
        cpu_values = [d['system']['cpu_percent'] for d in self.monitoring_data if d['system']]
        process_cpu_values = [d['process']['cpu_percent'] for d in self.monitoring_data 
                            if d['process'] and 'cpu_percent' in d['process']]
        
        # 메모리 사용률 통계
        memory_values = [d['system']['memory']['percent'] for d in self.monitoring_data if d['system']]
        process_memory_values = [d['process']['memory_percent'] for d in self.monitoring_data 
                               if d['process'] and 'memory_percent' in d['process']]
        
        # 연결 수 통계
        connection_values = [d['process']['connections'] for d in self.monitoring_data 
                           if d['process'] and 'connections' in d['process']]
        
        summary = {
            'monitoring_duration': time.time() - self.start_time if self.start_time else 0,
            'data_points': len(self.monitoring_data),
            'system_cpu': self._calculate_stats(cpu_values),
            'system_memory': self._calculate_stats(memory_values),
            'process_cpu': self._calculate_stats(process_cpu_values),
            'process_memory': self._calculate_stats(process_memory_values),
            'connections': self._calculate_stats(connection_values)
        }
        
        return summary
    
    def _calculate_stats(self, values: List[float]) -> Dict:
        """통계값 계산"""
        if not values:
            return {}
        
        return {
            'min': min(values),
            'max': max(values),
            'avg': sum(values) / len(values),
            'count': len(values)
        }
    
    def export_data(self, filename: str = None) -> str:
        """모니터링 데이터 내보내기"""
        if not filename:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"server_monitoring_{timestamp}.json"
        
        export_data = {
            'metadata': {
                'process_name': self.process_name,
                'start_time': self.start_time,
                'monitoring_duration': time.time() - self.start_time if self.start_time else 0,
                'data_points': len(self.monitoring_data)
            },
            'summary': self.get_summary_stats(),
            'data': self.monitoring_data
        }
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(export_data, f, indent=2, ensure_ascii=False)
            
            self.logger.info(f"Monitoring data exported to {filename}")
            return filename
            
        except Exception as e:
            self.logger.error(f"Failed to export data: {e}")
            return ""
    
    def check_server_port(self, port: int = 9200) -> bool:
        """서버 포트 연결 확인"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1.0)
            result = sock.connect_ex(('localhost', port))
            sock.close()
            return result == 0
        except:
            return False


class MonitoringReport:
    """모니터링 리포트 생성기"""
    
    @staticmethod
    def generate_report(monitor: ServerMonitor) -> str:
        """모니터링 리포트 생성"""
        summary = monitor.get_summary_stats()
        if not summary:
            return "모니터링 데이터가 없습니다."
        
        report = []
        report.append("=" * 60)
        report.append("서버 모니터링 리포트")
        report.append("=" * 60)
        
        # 기본 정보
        duration = summary['monitoring_duration']
        report.append(f"모니터링 시간: {duration:.1f}초 ({duration/60:.1f}분)")
        report.append(f"데이터 포인트: {summary['data_points']}개")
        report.append("")
        
        # 시스템 CPU
        if summary['system_cpu']:
            cpu = summary['system_cpu']
            report.append(f"시스템 CPU 사용률:")
            report.append(f"  평균: {cpu['avg']:.1f}%, 최소: {cpu['min']:.1f}%, 최대: {cpu['max']:.1f}%")
        
        # 시스템 메모리
        if summary['system_memory']:
            mem = summary['system_memory']
            report.append(f"시스템 메모리 사용률:")
            report.append(f"  평균: {mem['avg']:.1f}%, 최소: {mem['min']:.1f}%, 최대: {mem['max']:.1f}%")
        
        # 프로세스 CPU
        if summary['process_cpu']:
            proc_cpu = summary['process_cpu']
            report.append(f"서버 프로세스 CPU:")
            report.append(f"  평균: {proc_cpu['avg']:.1f}%, 최소: {proc_cpu['min']:.1f}%, 최대: {proc_cpu['max']:.1f}%")
        
        # 프로세스 메모리
        if summary['process_memory']:
            proc_mem = summary['process_memory']
            report.append(f"서버 프로세스 메모리:")
            report.append(f"  평균: {proc_mem['avg']:.1f}%, 최소: {proc_mem['min']:.1f}%, 최대: {proc_mem['max']:.1f}%")
        
        # 연결 수
        if summary['connections']:
            conn = summary['connections']
            report.append(f"동시 연결 수:")
            report.append(f"  평균: {conn['avg']:.1f}개, 최소: {conn['min']:.0f}개, 최대: {conn['max']:.0f}개")
        
        return "\n".join(report)


if __name__ == "__main__":
    import argparse
    import sys
    
    parser = argparse.ArgumentParser(description="서버 모니터링 도구")
    parser.add_argument("--process", default="ChattingServer.exe", help="모니터링할 프로세스 이름")
    parser.add_argument("--interval", type=float, default=1.0, help="업데이트 간격(초)")
    parser.add_argument("--duration", type=int, help="모니터링 시간(초)")
    parser.add_argument("--output", help="결과 저장 파일명")
    parser.add_argument("--port", type=int, default=9200, help="서버 포트 확인")
    
    args = parser.parse_args()
    
    monitor = ServerMonitor(args.process, args.interval)
    
    # 서버 포트 확인
    if not monitor.check_server_port(args.port):
        print(f"경고: 포트 {args.port}에서 서버를 찾을 수 없습니다.")
    
    try:
        if not monitor.start_monitoring():
            print("모니터링 시작 실패")
            sys.exit(1)
        
        print(f"서버 모니터링 시작 (프로세스: {args.process})")
        print("Ctrl+C로 중지")
        
        # 지정된 시간만큼 모니터링
        if args.duration:
            time.sleep(args.duration)
            monitor.stop_monitoring()
        else:
            # 무한 모니터링
            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                pass
    
    except KeyboardInterrupt:
        print("\n모니터링 중지됨")
    finally:
        monitor.stop_monitoring()
        
        # 최종 리포트
        print("\n" + MonitoringReport.generate_report(monitor))
        
        # 데이터 내보내기
        if args.output:
            monitor.export_data(args.output)
