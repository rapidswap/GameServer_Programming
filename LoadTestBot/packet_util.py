"""
패킷 유틸리티 - 패킷 인코딩/디코딩 기능
C# PacketUtil 클래스를 Python으로 포팅
"""

import struct
from io import BytesIO


class PacketUtil:
    """패킷 인코딩/디코딩 유틸리티 클래스"""
    
    @staticmethod
    def encode_header(packet_stream: BytesIO, header_type: int):
        """패킷 헤더 인코딩"""
        PacketUtil.encode_int64(packet_stream, header_type)
    
    @staticmethod
    def encode_byte(packet_stream: BytesIO, value: int):
        """1바이트 정수 인코딩"""
        packet_stream.write(struct.pack('<B', value))
    
    @staticmethod
    def encode_int16(packet_stream: BytesIO, value: int):
        """2바이트 정수 인코딩"""
        packet_stream.write(struct.pack('<h', value))
    
    @staticmethod
    def encode_uint16(packet_stream: BytesIO, value: int):
        """2바이트 부호없는 정수 인코딩"""
        packet_stream.write(struct.pack('<H', value))
    
    @staticmethod
    def encode_int32(packet_stream: BytesIO, value: int):
        """4바이트 정수 인코딩"""
        packet_stream.write(struct.pack('<i', value))
    
    @staticmethod
    def encode_uint32(packet_stream: BytesIO, value: int):
        """4바이트 부호없는 정수 인코딩"""
        packet_stream.write(struct.pack('<I', value))
    
    @staticmethod
    def encode_int64(packet_stream: BytesIO, value: int):
        """8바이트 정수 인코딩"""
        packet_stream.write(struct.pack('<q', value))
    
    @staticmethod
    def encode_uint64(packet_stream: BytesIO, value: int):
        """8바이트 부호없는 정수 인코딩"""
        packet_stream.write(struct.pack('<Q', value))
    
    @staticmethod
    def encode_string(packet_stream: BytesIO, value: str):
        """문자열 인코딩 (길이 + ASCII 바이트)"""
        ascii_bytes = value.encode('ascii', errors='replace')
        PacketUtil.encode_int32(packet_stream, len(ascii_bytes))
        packet_stream.write(ascii_bytes)
    
    # 디코딩 메소드들
    @staticmethod
    def decode_byte(data: bytes, offset: list) -> int:
        """1바이트 정수 디코딩"""
        result = struct.unpack_from('<B', data, offset[0])[0]
        offset[0] += 1
        return result
    
    @staticmethod
    def decode_int16(data: bytes, offset: list) -> int:
        """2바이트 정수 디코딩"""
        result = struct.unpack_from('<h', data, offset[0])[0]
        offset[0] += 2
        return result
    
    @staticmethod
    def decode_uint16(data: bytes, offset: list) -> int:
        """2바이트 부호없는 정수 디코딩"""
        result = struct.unpack_from('<H', data, offset[0])[0]
        offset[0] += 2
        return result
    
    @staticmethod
    def decode_int32(data: bytes, offset: list) -> int:
        """4바이트 정수 디코딩"""
        result = struct.unpack_from('<i', data, offset[0])[0]
        offset[0] += 4
        return result
    
    @staticmethod
    def decode_uint32(data: bytes, offset: list) -> int:
        """4바이트 부호없는 정수 디코딩"""
        result = struct.unpack_from('<I', data, offset[0])[0]
        offset[0] += 4
        return result
    
    @staticmethod
    def decode_int64(data: bytes, offset: list) -> int:
        """8바이트 정수 디코딩"""
        result = struct.unpack_from('<q', data, offset[0])[0]
        offset[0] += 8
        return result
    
    @staticmethod
    def decode_uint64(data: bytes, offset: list) -> int:
        """8바이트 부호없는 정수 디코딩"""
        result = struct.unpack_from('<Q', data, offset[0])[0]
        offset[0] += 8
        return result
    
    @staticmethod
    def decode_string(data: bytes, offset: list) -> str:
        """문자열 디코딩 (ASCII 사용)"""
        str_len = PacketUtil.decode_int32(data, offset)
        result = data[offset[0]:offset[0] + str_len].decode('ascii')
        offset[0] += str_len
        return result
    
    @staticmethod
    def decode_packet_type(data: bytes, offset: list) -> int:
        """패킷 타입 디코딩"""
        return PacketUtil.decode_int64(data, offset)
