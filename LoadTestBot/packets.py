"""
패킷 클래스들 - 각 패킷 타입별 클래스 정의
"""

import time
import struct
from io import BytesIO
from abc import ABC, abstractmethod
from packet_types import PacketType
from packet_util import PacketUtil


class PacketInterface(ABC):
    """패킷 인터페이스"""
    
    @abstractmethod
    def get_type(self) -> int:
        """패킷 타입 반환"""
        pass
    
    @abstractmethod
    def encode(self) -> bytes:
        """패킷 인코딩"""
        pass
    
    @abstractmethod
    def decode(self, data: bytes, offset: list):
        """패킷 디코딩"""
        pass


class ChatNameRegistrationPacket(PacketInterface):
    """채팅 이름 등록 패킷"""
    
    def __init__(self, name: str = ""):
        self.name = name
    
    def get_type(self) -> int:
        return PacketType.E_C_REQ_REGIST_CHATTING_NAME
    
    def encode(self) -> bytes:
        """패킷 인코딩 (올바른 형식)"""
        # 패킷 데이터 생성
        data_stream = BytesIO()
        PacketUtil.encode_header(data_stream, self.get_type())
        PacketUtil.encode_string(data_stream, self.name)
        packet_data = data_stream.getvalue()
        
        # 패킷 길이 계산 (4바이트 헤더 + 데이터 크기)
        packet_length = 4 + len(packet_data)
        
        # 최종 패킷 조립
        from packet_obfuscation import PacketObfuscation
        final_stream = BytesIO()
        
        # 1. 패킷 길이 헤더 (암호화)
        header_bytes = struct.pack('<i', packet_length)
        encrypted_header = PacketObfuscation.encoding_header(header_bytes)
        final_stream.write(encrypted_header)
        
        # 2. 패킷 데이터 (암호화)
        encrypted_data = PacketObfuscation.encoding_data(packet_data)
        final_stream.write(encrypted_data)
        
        return final_stream.getvalue()
    
    def decode(self, data: bytes, offset: list):
        self.name = PacketUtil.decode_string(data, offset)


class ChatMessagePacket(PacketInterface):
    """채팅 메시지 패킷"""
    
    def __init__(self, text: str = "", client_timestamp: int = 0):
        self.text = text
        self.client_timestamp = client_timestamp if client_timestamp else int(time.time() * 1000)
    
    def get_type(self) -> int:
        return PacketType.E_C_REQ_CHATTING
    
    def encode(self) -> bytes:
        """패킷 인코딩 (올바른 형식)"""
        # 패킷 데이터 생성
        data_stream = BytesIO()
        PacketUtil.encode_header(data_stream, self.get_type())
        PacketUtil.encode_string(data_stream, self.text)
        PacketUtil.encode_uint64(data_stream, self.client_timestamp)
        packet_data = data_stream.getvalue()
        
        # 패킷 길이 계산
        packet_length = 4 + len(packet_data)
        
        # 최종 패킷 조립
        from packet_obfuscation import PacketObfuscation
        final_stream = BytesIO()
        
        # 1. 패킷 길이 헤더 (암호화)
        header_bytes = struct.pack('<i', packet_length)
        encrypted_header = PacketObfuscation.encoding_header(header_bytes)
        final_stream.write(encrypted_header)
        
        # 2. 패킷 데이터 (암호화)
        encrypted_data = PacketObfuscation.encoding_data(packet_data)
        final_stream.write(encrypted_data)
        
        return final_stream.getvalue()
    
    def decode(self, data: bytes, offset: list):
        self.text = PacketUtil.decode_string(data, offset)
        self.client_timestamp = PacketUtil.decode_uint64(data, offset)


class ChatResponsePacket(PacketInterface):
    """채팅 응답 패킷"""
    
    def __init__(self):
        self.name = ""
        self.text = ""
        self.server_timestamp = 0
    
    def get_type(self) -> int:
        return PacketType.E_S_ANS_CHATTING
    
    def encode(self) -> bytes:
        stream = BytesIO()
        PacketUtil.encode_header(stream, self.get_type())
        PacketUtil.encode_string(stream, self.name)
        PacketUtil.encode_string(stream, self.text)
        PacketUtil.encode_uint64(stream, self.server_timestamp)
        return stream.getvalue()
    
    def decode(self, data: bytes, offset: list):
        self.name = PacketUtil.decode_string(data, offset)
        self.text = PacketUtil.decode_string(data, offset)
        self.server_timestamp = PacketUtil.decode_uint64(data, offset)


class NewUserNotifyPacket(PacketInterface):
    """새 사용자 알림 패킷"""
    
    def __init__(self):
        self.name = ""
    
    def get_type(self) -> int:
        return PacketType.E_S_ANS_NEW_USER_NOTIFY
    
    def encode(self) -> bytes:
        stream = BytesIO()
        PacketUtil.encode_header(stream, self.get_type())
        PacketUtil.encode_string(stream, self.name)
        return stream.getvalue()
    
    def decode(self, data: bytes, offset: list):
        self.name = PacketUtil.decode_string(data, offset)


class UserListPacket(PacketInterface):
    """사용자 목록 패킷"""
    
    def __init__(self):
        self.names = []
    
    def get_type(self) -> int:
        return PacketType.E_S_ANS_USER_LIST
    
    def encode(self) -> bytes:
        stream = BytesIO()
        PacketUtil.encode_header(stream, self.get_type())
        PacketUtil.encode_int32(stream, len(self.names))
        for name in self.names:
            PacketUtil.encode_string(stream, name)
        return stream.getvalue()
    
    def decode(self, data: bytes, offset: list):
        count = PacketUtil.decode_int32(data, offset)
        self.names = []
        for _ in range(count):
            name = PacketUtil.decode_string(data, offset)
            self.names.append(name)


class ExitUserPacket(PacketInterface):
    """사용자 퇴장 패킷"""
    
    def __init__(self):
        self.name = ""
    
    def get_type(self) -> int:
        return PacketType.E_S_ANS_EXIT_USER
    
    def encode(self) -> bytes:
        stream = BytesIO()
        PacketUtil.encode_header(stream, self.get_type())
        PacketUtil.encode_string(stream, self.name)
        return stream.getvalue()
    
    def decode(self, data: bytes, offset: list):
        self.name = PacketUtil.decode_string(data, offset)


class ChatExitPacket(PacketInterface):
    """채팅 퇴장 요청 패킷"""
    
    def __init__(self):
        pass
    
    def get_type(self) -> int:
        return PacketType.E_C_REQ_CHAT_EXIT
    
    def encode(self) -> bytes:
        stream = BytesIO()
        PacketUtil.encode_header(stream, self.get_type())
        return stream.getvalue()
    
    def decode(self, data: bytes, offset: list):
        pass


class PingPacket(PacketInterface):
    """핑 패킷"""
    
    def __init__(self, client_timestamp: int = 0, sequence_number: int = 0):
        self.client_timestamp = client_timestamp if client_timestamp else int(time.time() * 1000)
        self.sequence_number = sequence_number
    
    def get_type(self) -> int:
        return PacketType.E_C_REQ_PING
    
    def encode(self) -> bytes:
        stream = BytesIO()
        PacketUtil.encode_header(stream, self.get_type())
        PacketUtil.encode_uint64(stream, self.client_timestamp)
        PacketUtil.encode_uint32(stream, self.sequence_number)
        return stream.getvalue()
    
    def decode(self, data: bytes, offset: list):
        self.client_timestamp = PacketUtil.decode_uint64(data, offset)
        self.sequence_number = PacketUtil.decode_uint32(data, offset)


class PongPacket(PacketInterface):
    """퐁 패킷"""
    
    def __init__(self):
        self.client_timestamp = 0
        self.server_timestamp = 0
        self.sequence_number = 0
    
    def get_type(self) -> int:
        return PacketType.E_S_ANS_PONG
    
    def encode(self) -> bytes:
        stream = BytesIO()
        PacketUtil.encode_header(stream, self.get_type())
        PacketUtil.encode_uint64(stream, self.client_timestamp)
        PacketUtil.encode_uint64(stream, self.server_timestamp)
        PacketUtil.encode_uint32(stream, self.sequence_number)
        return stream.getvalue()
    
    def decode(self, data: bytes, offset: list):
        self.client_timestamp = PacketUtil.decode_uint64(data, offset)
        self.server_timestamp = PacketUtil.decode_uint64(data, offset)
        self.sequence_number = PacketUtil.decode_uint32(data, offset)


class PacketFactory:
    """패킷 팩토리 클래스"""
    
    PACKET_MAP = {
        PacketType.E_S_ANS_CHATTING: ChatResponsePacket,
        PacketType.E_S_ANS_NEW_USER_NOTIFY: NewUserNotifyPacket,
        PacketType.E_S_ANS_USER_LIST: UserListPacket,
        PacketType.E_S_ANS_EXIT_USER: ExitUserPacket,
        PacketType.E_S_ANS_PONG: PongPacket,
    }
    
    @staticmethod
    def create_packet(packet_type: int) -> PacketInterface:
        """패킷 타입에 따른 패킷 객체 생성"""
        packet_class = PacketFactory.PACKET_MAP.get(packet_type)
        if packet_class:
            return packet_class()
        return None
    
    @staticmethod
    def parse_packet(data: bytes) -> PacketInterface:
        """바이트 데이터를 패킷 객체로 파싱 (암호화된 패킷 처리)"""
        if len(data) < 4:  # 최소 헤더 크기
            return None
            
        try:
            from packet_obfuscation import PacketObfuscation
            
            # 1. 헤더 복호화 (패킷 길이)
            encrypted_header = data[:4]
            decrypted_header = PacketObfuscation.decoding_header(encrypted_header)
            packet_length = struct.unpack('<i', decrypted_header)[0]
            
            if len(data) < packet_length:
                return None  # 불완전한 패킷
            
            # 2. 데이터 복호화
            encrypted_data = data[4:packet_length]
            decrypted_data = PacketObfuscation.decoding_data(encrypted_data)
            
            # 3. 패킷 타입 추출
            if len(decrypted_data) < 8:
                return None
                
            offset = [0]
            packet_type = PacketUtil.decode_packet_type(decrypted_data, offset)
            packet = PacketFactory.create_packet(packet_type)
            
            if packet and offset[0] < len(decrypted_data):
                packet.decode(decrypted_data, offset)
            
            return packet
            
        except Exception as e:
            # 파싱 실패
            return None
