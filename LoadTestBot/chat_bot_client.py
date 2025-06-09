"""
채팅 봇 클라이언트 - 개별 봇 인스턴스
"""

import socket
import threading
import time
import random
import logging
import struct
from typing import Optional, Callable
from packets import *
from packet_util import PacketUtil


class ChatBotClient:
    """개별 채팅 봇 클라이언트"""
    
    def __init__(self, bot_id: int, server_host: str, server_port: int, 
                 message_callback: Optional[Callable] = None,
                 latency_callback: Optional[Callable] = None):
        self.bot_id = bot_id
        self.server_host = server_host
        self.server_port = server_port
        self.name = f"Bot_{bot_id:04d}"
        
        # 콜백 함수들
        self.message_callback = message_callback
        self.latency_callback = latency_callback
        
        # 네트워크
        self.socket: Optional[socket.socket] = None
        self.connected = False
        self.running = False
        
        # 스레드
        self.receive_thread: Optional[threading.Thread] = None
        self.message_thread: Optional[threading.Thread] = None
        self.ping_thread: Optional[threading.Thread] = None
        
        # 통계
        self.messages_sent = 0
        self.messages_received = 0
        self.ping_sequence = 0
        self.last_ping_time = 0
        self.ping_responses = {}
        
        # 봇 설정
        self.message_interval = random.uniform(3.0, 8.0)  # 3-8초 랜덤 간격
        self.ping_interval = 30.0  # 30초마다 핑
        
        # 로깅
        self.logger = logging.getLogger(f"Bot_{bot_id}")
        
        # 채팅 메시지 풀
        self.chat_messages = [
            "안녕하세요! 🎮",
            "게임 서버 테스트 중입니다.",
            "오늘 날씨가 좋네요 ☀️",
            "부하테스트 진행 중...",
            "서버 성능이 어떤가요?",
            "채팅이 잘 되고 있나요?",
            "Load Testing Bot 입니다!",
            "서버 응답속도 체크 중 📊",
            "안정성 테스트 진행중",
            "여러분들 잘 지내시죠? 😊",
            "봇이지만 열심히 일하고 있어요",
            "실시간 채팅 테스트!",
            "서버 동시접속 테스트 중",
            "성능 모니터링 중... 📈",
            "채팅서버 스트레스 테스트"
        ]
    
    def connect(self) -> bool:
        """서버에 연결"""
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.settimeout(10.0)  # 10초 타임아웃
            self.socket.connect((self.server_host, self.server_port))
            self.connected = True
            self.running = True
            
            self.logger.info(f"Bot {self.name} connected to {self.server_host}:{self.server_port}")
            
            # 이름 등록
            self._register_name()
            
            # 수신 스레드 시작
            self.receive_thread = threading.Thread(target=self._receive_loop, daemon=True)
            self.receive_thread.start()
            
            # 메시지 전송 스레드 시작
            self.message_thread = threading.Thread(target=self._message_loop, daemon=True)
            self.message_thread.start()
            
            # 하트비트 스레드 시작
            self.heartbeat_thread = threading.Thread(target=self._heartbeat_loop, daemon=True)
            self.heartbeat_thread.start()
            
            return True
            
        except Exception as e:
            self.logger.error(f"Bot {self.name} connection failed: {e}")
            self.connected = False
            return False
    
    def disconnect(self):
        """서버 연결 해제"""
        self.running = False
        
        if self.connected and self.socket:
            try:
                # 퇴장 패킷 전송
                exit_packet = ChatExitPacket()
                self._send_packet(exit_packet)
                time.sleep(0.1)  # 전송 완료 대기
            except:
                pass
        
        if self.socket:
            try:
                self.socket.close()
            except:
                pass
            
        self.connected = False
        self.logger.info(f"Bot {self.name} disconnected")
    
    def _register_name(self):
        """이름 등록"""
        try:
            packet = ChatNameRegistrationPacket(self.name)
            self._send_packet(packet)
            self.logger.info(f"Bot {self.name} registered name")
        except Exception as e:
            self.logger.error(f"Bot {self.name} failed to register name: {e}")
    
    def _send_packet(self, packet: PacketInterface):
        """패킷 전송"""
        if not self.connected or not self.socket:
            return
            
        try:
            # 소켓 상태 확인
            if self.socket.fileno() == -1:
                self.logger.warning(f"Bot {self.name} socket closed, marking as disconnected")
                self.connected = False
                return
                
            data = packet.encode()
            self.socket.send(data)
        except (ConnectionResetError, ConnectionAbortedError, OSError) as e:
            self.logger.warning(f"Bot {self.name} connection lost: {e}")
            self.connected = False
        except Exception as e:
            self.logger.error(f"Bot {self.name} failed to send packet: {e}")
            self.connected = False
    
    def _receive_loop(self):
        """패킷 수신 루프 (암호화 지원)"""
        buffer = b""
        
        while self.running and self.connected:
            try:
                # 소켓 상태 확인
                if self.socket.fileno() == -1:
                    self.logger.warning(f"Bot {self.name} socket closed during receive")
                    break
                    
                data = self.socket.recv(4096)
                if not data:
                    self.logger.info(f"Bot {self.name} received empty data, connection closed")
                    break
                    
                buffer += data
                
                # 패킷 파싱
                while len(buffer) >= 4:  # 최소 헤더 크기
                    try:
                        from packet_obfuscation import PacketObfuscation
                        
                        # 헤더를 복호화하여 패킷 길이 확인
                        encrypted_header = buffer[:4]
                        decrypted_header = PacketObfuscation.decoding_header(encrypted_header)
                        packet_length = struct.unpack('<i', decrypted_header)[0]
                        
                        # 전체 패킷이 도착했는지 확인
                        if len(buffer) < packet_length:
                            break  # 더 많은 데이터 필요
                        
                        # 완전한 패킷 추출
                        packet_data = buffer[:packet_length]
                        buffer = buffer[packet_length:]
                        
                        # 패킷 파싱
                        packet = PacketFactory.parse_packet(packet_data)
                        if packet:
                            self._handle_packet(packet)
                        
                    except Exception as e:
                        self.logger.warning(f"Packet parsing error: {e}")
                        # 첫 바이트 제거하고 재시도
                        if len(buffer) > 0:
                            buffer = buffer[1:]
                        break
                        
            except socket.timeout:
                continue
            except (ConnectionResetError, ConnectionAbortedError, OSError) as e:
                self.logger.warning(f"Bot {self.name} connection lost during receive: {e}")
                break
            except Exception as e:
                if self.running:
                    self.logger.error(f"Bot {self.name} receive error: {e}")
                break
        
        self.connected = False
    
    def _handle_packet(self, packet: PacketInterface):
        """수신된 패킷 처리"""
        if isinstance(packet, ChatResponsePacket):
            self.messages_received += 1
            if self.message_callback:
                self.message_callback(self.bot_id, packet.name, packet.text)
                
        elif isinstance(packet, PongPacket):
            if packet.sequence_number in self.ping_responses:
                current_time = int(time.time() * 1000)
                latency = current_time - packet.client_timestamp
                del self.ping_responses[packet.sequence_number]
                
                if self.latency_callback:
                    self.latency_callback(self.bot_id, latency)
                    
        elif isinstance(packet, NewUserNotifyPacket):
            self.logger.debug(f"New user joined: {packet.name}")
            
        elif isinstance(packet, ExitUserPacket):
            self.logger.debug(f"User left: {packet.name}")
            
        elif isinstance(packet, UserListPacket):
            self.logger.debug(f"User list: {packet.names}")
    
    def _message_loop(self):
        """메시지 전송 루프"""
        while self.running and self.connected:
            try:
                time.sleep(self.message_interval)
                
                if not self.running or not self.connected:
                    break
                
                # 랜덤 메시지 선택
                message = random.choice(self.chat_messages)
                if random.random() < 0.3:  # 30% 확률로 봇 정보 추가
                    message += f" (Bot #{self.bot_id})"
                
                # 채팅 메시지 전송
                chat_packet = ChatMessagePacket(message)
                self._send_packet(chat_packet)
                self.messages_sent += 1
                
                # 다음 메시지 간격 재설정
                self.message_interval = random.uniform(3.0, 8.0)
                
            except Exception as e:
                if self.running:
                    self.logger.error(f"Bot {self.name} message loop error: {e}")
                break
    
    def _heartbeat_loop(self):
        """하트비트 전송 루프 (1초마다)"""
        while self.running and self.connected:
            try:
                time.sleep(1.0)  # 1초마다 전송
                
                if not self.running or not self.connected:
                    break
                
                # 하트비트 전송
                from packets import HeartbeatPacket
                heartbeat_packet = HeartbeatPacket()
                self._send_packet(heartbeat_packet)
                
            except Exception as e:
                if self.running:
                    self.logger.error(f"Bot {self.name} heartbeat loop error: {e}")
                break
    
    def _ping_loop(self):
        """핑 전송 루프"""
        while self.running and self.connected:
            try:
                time.sleep(self.ping_interval)
                
                if not self.running or not self.connected:
                    break
                
                # 핑 전송
                self.ping_sequence += 1
                ping_packet = PingPacket(sequence_number=self.ping_sequence)
                self.ping_responses[self.ping_sequence] = time.time()
                self._send_packet(ping_packet)
                
            except Exception as e:
                if self.running:
                    self.logger.error(f"Bot {self.name} ping loop error: {e}")
                break
    
    def get_stats(self) -> dict:
        """봇 통계 반환"""
        return {
            'bot_id': self.bot_id,
            'name': self.name,
            'connected': self.connected,
            'messages_sent': self.messages_sent,
            'messages_received': self.messages_received,
            'pending_pings': len(self.ping_responses)
        }
    
    def send_custom_message(self, message: str):
        """사용자 정의 메시지 전송"""
        if self.connected:
            chat_packet = ChatMessagePacket(message)
            self._send_packet(chat_packet)
            self.messages_sent += 1
