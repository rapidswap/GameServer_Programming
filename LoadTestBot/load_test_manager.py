"""
부하테스트 매니저 - 여러 봇을 관리하고 통계를 수집
"""

import time
import threading
import logging
import json
from typing import List, Dict, Any
from datetime import datetime
from chat_bot_client import ChatBotClient


class LoadTestManager:
    """부하테스트 매니저 클래스"""
    
    def __init__(self, server_host: str = "localhost", server_port: int = 9200):
        self.server_host = server_host
        self.server_port = server_port
        
        # 봇 관리
        self.bots: List[ChatBotClient] = []
        self.max_bots = 0
        self.connected_bots = 0
        
        # 통계
        self.total_messages_sent = 0
        self.total_messages_received = 0
        self.latency_samples = []
        self.error_count = 0
        
        # 테스트 설정
        self.test_running = False
        self.test_start_time = None
        self.test_duration = 0
        
        # 스레드
        self.monitor_thread: threading.Thread = None
        self.stats_lock = threading.Lock()
        
        # 로깅
        self.logger = logging.getLogger("LoadTestManager")
        self._setup_logging()
    
    def _setup_logging(self):
        """로깅 설정"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.StreamHandler(),
                logging.FileHandler('load_test.log')
            ]
        )
    
    def create_bots(self, count: int) -> bool:
        """지정된 수만큼 봇 생성"""
        try:
            self.max_bots = count
            self.bots = []
            
            for i in range(count):
                bot = ChatBotClient(
                    bot_id=i + 1,
                    server_host=self.server_host,
                    server_port=self.server_port,
                    message_callback=self._on_message_received,
                    latency_callback=self._on_latency_measured
                )
                self.bots.append(bot)
            
            self.logger.info(f"Created {count} bots")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to create bots: {e}")
            return False
    
    def start_test(self, test_duration_seconds: int = 0) -> bool:
        """부하테스트 시작"""
        try:
            if self.test_running:
                self.logger.warning("Test is already running")
                return False
            
            self.test_running = True
            self.test_start_time = time.time()
            self.test_duration = test_duration_seconds
            self.connected_bots = 0
            
            # 통계 초기화
            with self.stats_lock:
                self.total_messages_sent = 0
                self.total_messages_received = 0
                self.latency_samples = []
                self.error_count = 0
            
            self.logger.info(f"Starting load test with {len(self.bots)} bots")
            
            # 봇들을 순차적으로 연결 (동시 연결 부하 방지)
            connection_thread = threading.Thread(target=self._connect_bots_gradually, daemon=True)
            connection_thread.start()
            
            # 모니터링 스레드 시작
            self.monitor_thread = threading.Thread(target=self._monitor_loop, daemon=True)
            self.monitor_thread.start()
            
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to start test: {e}")
            self.test_running = False
            return False
    
    def stop_test(self):
        """부하테스트 중지"""
        self.logger.info("Stopping load test...")
        self.test_running = False
        
        # 모든 봇 연결 해제
        for bot in self.bots:
            try:
                bot.disconnect()
            except Exception as e:
                self.logger.error(f"Error disconnecting bot {bot.bot_id}: {e}")
        
        self.connected_bots = 0
        self.logger.info("Load test stopped")
    
    def _connect_bots_gradually(self):
        """봇들을 점진적으로 연결 (봇 수에 따른 적응적 배치)"""
        total_bots = len(self.bots)
        
        # 봇 수에 따른 배치 크기 조정
        if total_bots <= 10:
            batch_size = 2  # 10개 이하는 2개씩
            batch_delay = 3.0  # 3초 대기
            bot_delay = 1.0  # 1초 대기
        elif total_bots <= 50:
            batch_size = 5  # 50개 이하는 5개씩
            batch_delay = 2.0  # 2초 대기
            bot_delay = 0.5  # 0.5초 대기
        else:
            batch_size = 10  # 50개 이상은 10개씩
            batch_delay = 1.0  # 1초 대기
            bot_delay = 0.3  # 0.3초 대기
        
        self.logger.info(f"Connecting {total_bots} bots in batches of {batch_size} (delays: batch={batch_delay}s, bot={bot_delay}s)")
        
        for i in range(0, len(self.bots), batch_size):
            if not self.test_running:
                break
            
            # 현재 배치의 봇들
            batch_end = min(i + batch_size, len(self.bots))
            current_batch = self.bots[i:batch_end]
            
            self.logger.info(f"Connecting batch {i//batch_size + 1}: bots {i+1}-{batch_end}")
            
            # 배치 내 봇들을 순차적으로 연결
            for bot in current_batch:
                if not self.test_running:
                    break
                
                try:
                    if bot.connect():
                        self.connected_bots += 1
                        self.logger.info(f"Bot {bot.bot_id} connected ({self.connected_bots}/{len(self.bots)})")
                    else:
                        self.error_count += 1
                        self.logger.error(f"Bot {bot.bot_id} failed to connect")
                    
                    # 봇 간 대기 (마지막 봇이 아닌 경우)
                    if bot != current_batch[-1]:
                        time.sleep(bot_delay)
                        
                except Exception as e:
                    self.logger.error(f"Error connecting bot {bot.bot_id}: {e}")
                    self.error_count += 1
            
            # 배치 간 대기 (마지막 배치가 아닌 경우)
            if batch_end < len(self.bots) and self.test_running:
                self.logger.info(f"Waiting {batch_delay}s before next batch...")
                time.sleep(batch_delay)
    
    def _monitor_loop(self):
        """모니터링 루프"""
        while self.test_running:
            try:
                time.sleep(5)  # 5초마다 모니터링
                
                if not self.test_running:
                    break
                
                # 통계 수집 및 출력
                stats = self.get_current_stats()
                self._print_stats(stats)
                
                # 테스트 시간 확인
                if self.test_duration > 0:
                    elapsed = time.time() - self.test_start_time
                    if elapsed >= self.test_duration:
                        self.logger.info(f"Test duration ({self.test_duration}s) reached")
                        self.stop_test()
                        break
                
            except Exception as e:
                self.logger.error(f"Monitor loop error: {e}")
    
    def _on_message_received(self, bot_id: int, sender_name: str, message: str):
        """메시지 수신 콜백"""
        with self.stats_lock:
            self.total_messages_received += 1
    
    def _on_latency_measured(self, bot_id: int, latency_ms: int):
        """레이턴시 측정 콜백"""
        with self.stats_lock:
            self.latency_samples.append(latency_ms)
            # 최근 100개 샘플만 유지
            if len(self.latency_samples) > 100:
                self.latency_samples = self.latency_samples[-100:]
    
    def get_current_stats(self) -> Dict[str, Any]:
        """현재 통계 반환"""
        with self.stats_lock:
            # 봇별 통계 수집
            bot_stats = []
            total_sent = 0
            total_received = 0
            active_bots = 0
            
            for bot in self.bots:
                stats = bot.get_stats()
                bot_stats.append(stats)
                total_sent += stats['messages_sent']
                total_received += stats['messages_received']
                if stats['connected']:
                    active_bots += 1
            
            # 레이턴시 통계
            latency_stats = {}
            if self.latency_samples:
                latency_stats = {
                    'min': min(self.latency_samples),
                    'max': max(self.latency_samples),
                    'avg': sum(self.latency_samples) / len(self.latency_samples),
                    'samples': len(self.latency_samples)
                }
            
            # 테스트 시간
            elapsed_time = time.time() - self.test_start_time if self.test_start_time else 0
            
            return {
                'test_running': self.test_running,
                'elapsed_time': elapsed_time,
                'total_bots': len(self.bots),
                'connected_bots': active_bots,
                'messages_sent': total_sent,
                'messages_received': total_received,
                'error_count': self.error_count,
                'latency': latency_stats,
                'bot_details': bot_stats
            }
    
    def _print_stats(self, stats: Dict[str, Any]):
        """통계 출력"""
        print("\n" + "="*80)
        print(f"부하테스트 상태 - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*80)
        print(f"테스트 시간: {stats['elapsed_time']:.1f}초")
        print(f"봇 상태: {stats['connected_bots']}/{stats['total_bots']} 연결됨")
        print(f"메시지: 전송 {stats['messages_sent']}, 수신 {stats['messages_received']}")
        print(f"오류 수: {stats['error_count']}")
        
        if stats['latency']:
            lat = stats['latency']
            print(f"레이턴시: 평균 {lat['avg']:.1f}ms, 최소 {lat['min']}ms, 최대 {lat['max']}ms")
        
        # 초당 메시지 처리량
        if stats['elapsed_time'] > 0:
            msg_per_sec = stats['messages_sent'] / stats['elapsed_time']
            print(f"처리량: {msg_per_sec:.1f} 메시지/초")
    
    def export_stats(self, filename: str = None) -> str:
        """통계를 JSON 파일로 내보내기"""
        if not filename:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"load_test_stats_{timestamp}.json"
        
        stats = self.get_current_stats()
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(stats, f, indent=2, ensure_ascii=False)
            
            self.logger.info(f"Stats exported to {filename}")
            return filename
            
        except Exception as e:
            self.logger.error(f"Failed to export stats: {e}")
            return ""
    
    def send_broadcast_message(self, message: str):
        """모든 봇에게 브로드캐스트 메시지 전송"""
        sent_count = 0
        for bot in self.bots:
            if bot.connected:
                try:
                    bot.send_custom_message(message)
                    sent_count += 1
                except Exception as e:
                    self.logger.error(f"Failed to send broadcast to bot {bot.bot_id}: {e}")
        
        self.logger.info(f"Broadcast message sent to {sent_count} bots: {message}")
        return sent_count
    
    def get_bot_by_id(self, bot_id: int) -> ChatBotClient:
        """ID로 봇 찾기"""
        for bot in self.bots:
            if bot.bot_id == bot_id:
                return bot
        return None
