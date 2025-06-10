"""
패킷 생성 유틸리티 - C# Network.sendPacket()과 정확히 동일한 방식
"""

import struct
from io import BytesIO
from packet_obfuscation import PacketObfuscation


def create_network_packet(packet_interface) -> bytes:
    """
    C# Network.sendPacket()과 정확히 동일한 방식으로 패킷 생성
    """
    try:
        # 1. 패킷 인코딩 (기본 데이터만)
        packet_data = packet_interface.encode_raw()  # 암호화 없는 순수 데이터
        
        # 2. 패킷 길이 계산 (4바이트 헤더 + 데이터 길이)
        packet_length = 4 + len(packet_data)  # sizeof(Int32) + packet.getStream().Length
        
        # 3. 패킷 블록 생성
        packet_block = BytesIO()
        
        # 4. 패킷 헤더 (길이) 암호화 후 추가
        header_bytes = struct.pack('<i', packet_length)
        encrypted_header = PacketObfuscation.encoding_header(header_bytes)
        packet_block.write(encrypted_header)
        
        # 5. 패킷 데이터 암호화 후 추가
        encrypted_data = PacketObfuscation.encoding_data(packet_data)
        packet_block.write(encrypted_data)
        
        return packet_block.getvalue()
        
    except Exception as e:
        print(f"Packet creation error: {e}")
        return b""
