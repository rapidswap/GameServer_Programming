"""
패킷 암호화/난독화 - C# PacketObfuscation 포팅
"""

class PacketObfuscation:
    """패킷 암호화/난독화 클래스"""
    
    # C#에서 PacketMakeDate.stamp() 값과 동일해야 함
    PACKET_MAKE_DATE = "2025/03/01 12:13:55"
    
    @classmethod
    def _get_key(cls) -> bytes:
        """암호화 키 생성"""
        return cls.PACKET_MAKE_DATE.encode('ascii')
    
    @classmethod
    def _calc_xor(cls, packet: bytearray, packet_offset: int, packet_len: int):
        """XOR 암호화/복호화"""
        key = cls._get_key()
        key_idx = packet_offset % len(key)
        
        for packet_idx in range(packet_len):
            packet[packet_idx] ^= key[key_idx]
            key_idx += 1
            if key_idx == len(key):
                key_idx = 0
    
    @classmethod
    def encoding_header(cls, packet: bytes) -> bytes:
        """헤더 암호화"""
        packet_array = bytearray(packet)
        cls._calc_xor(packet_array, 0, len(packet_array))
        return bytes(packet_array)
    
    @classmethod
    def encoding_data(cls, packet: bytes) -> bytes:
        """데이터 암호화"""
        packet_array = bytearray(packet)
        cls._calc_xor(packet_array, 4, len(packet_array))  # sizeof(Int32) = 4
        return bytes(packet_array)
    
    @classmethod
    def decoding_header(cls, packet: bytes) -> bytes:
        """헤더 복호화"""
        packet_array = bytearray(packet)
        cls._calc_xor(packet_array, 0, len(packet_array))
        return bytes(packet_array)
    
    @classmethod
    def decoding_data(cls, packet: bytes) -> bytes:
        """데이터 복호화"""
        packet_array = bytearray(packet)
        cls._calc_xor(packet_array, 4, len(packet_array))  # sizeof(Int32) = 4
        return bytes(packet_array)
