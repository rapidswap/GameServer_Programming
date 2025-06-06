"""
간단한 테스트 클라이언트 - 연결 테스트 및 디버깅용
"""

import socket
import time
import struct
from io import BytesIO
from packet_types import PacketType
from packet_obfuscation import PacketObfuscation


def create_name_registration_packet(name: str) -> bytes:
    """이름 등록 패킷 생성 (올바른 형식)"""
    # 패킷 데이터 생성
    data_stream = BytesIO()
    
    # 패킷 타입 (8바이트)
    data_stream.write(struct.pack('<q', PacketType.E_C_REQ_REGIST_CHATTING_NAME))
    
    # 문자열 길이 (4바이트) + 문자열 데이터
    name_bytes = name.encode('ascii', errors='replace')
    data_stream.write(struct.pack('<i', len(name_bytes)))
    data_stream.write(name_bytes)
    
    packet_data = data_stream.getvalue()
    
    # 패킷 길이 계산 (4바이트 헤더 + 데이터 크기)
    packet_length = 4 + len(packet_data)
    
    # 최종 패킷 조립
    final_stream = BytesIO()
    
    # 1. 패킷 길이 헤더 (암호화)
    header_bytes = struct.pack('<i', packet_length)
    encrypted_header = PacketObfuscation.encoding_header(header_bytes)
    final_stream.write(encrypted_header)
    
    # 2. 패킷 데이터 (암호화)
    encrypted_data = PacketObfuscation.encoding_data(packet_data)
    final_stream.write(encrypted_data)
    
    return final_stream.getvalue()


def create_chat_message_packet(text: str) -> bytes:
    """채팅 메시지 패킷 생성 (올바른 형식)"""
    # 패킷 데이터 생성
    data_stream = BytesIO()
    
    # 패킷 타입 (8바이트)
    data_stream.write(struct.pack('<q', PacketType.E_C_REQ_CHATTING))
    
    # 텍스트 (문자열)
    text_bytes = text.encode('ascii', errors='replace')
    data_stream.write(struct.pack('<i', len(text_bytes)))
    data_stream.write(text_bytes)
    
    # 클라이언트 타임스탬프 (8바이트)
    timestamp = int(time.time() * 1000)
    data_stream.write(struct.pack('<Q', timestamp))
    
    packet_data = data_stream.getvalue()
    
    # 패킷 길이 계산
    packet_length = 4 + len(packet_data)
    
    # 최종 패킷 조립
    final_stream = BytesIO()
    
    # 1. 패킷 길이 헤더 (암호화)
    header_bytes = struct.pack('<i', packet_length)
    encrypted_header = PacketObfuscation.encoding_header(header_bytes)
    final_stream.write(encrypted_header)
    
    # 2. 패킷 데이터 (암호화)
    encrypted_data = PacketObfuscation.encoding_data(packet_data)
    final_stream.write(encrypted_data)
    
    return final_stream.getvalue()


def simple_test():
    """간단한 연결 테스트"""
    try:
        # 서버 연결
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5.0)
        
        print("서버에 연결 중...")
        sock.connect(('localhost', 9200))
        print("연결 성공!")
        
        # 이름 등록
        print("이름 등록 중...")
        name_packet = create_name_registration_packet("TestBot_001")
        print(f"Name packet size: {len(name_packet)} bytes")
        print(f"Name packet hex: {name_packet.hex()}")
        
        sock.send(name_packet)
        print("이름 등록 패킷 전송 완료")
        
        # 잠시 대기
        time.sleep(1)
        
        # 채팅 메시지 전송
        print("채팅 메시지 전송 중...")
        chat_packet = create_chat_message_packet("Hello from Python Bot!")
        print(f"Chat packet size: {len(chat_packet)} bytes")
        print(f"Chat packet hex: {chat_packet.hex()}")
        
        sock.send(chat_packet)
        print("채팅 메시지 전송 완료")
        
        # 응답 대기
        print("서버 응답 대기 중...")
        sock.settimeout(3.0)
        
        try:
            response = sock.recv(1024)
            if response:
                print(f"응답 받음: {len(response)} bytes")
                print(f"Response hex: {response.hex()}")
                
                # 응답 패킷 파싱
                if len(response) >= 4:
                    # 1. 헤더 복호화 (패킷 길이)
                    encrypted_header = response[:4]
                    decrypted_header = PacketObfuscation.decoding_header(encrypted_header)
                    packet_length = struct.unpack('<i', decrypted_header)[0]
                    print(f"Packet length: {packet_length}")
                    
                    # 2. 데이터 복호화
                    if len(response) >= packet_length:
                        encrypted_data = response[4:packet_length]
                        decrypted_data = PacketObfuscation.decoding_data(encrypted_data)
                        
                        # 3. 패킷 타입 확인
                        if len(decrypted_data) >= 8:
                            packet_type = struct.unpack('<q', decrypted_data[:8])[0]
                            print(f"Decrypted packet type: {packet_type}")
                            
                            # 사용자 목록 패킷인지 확인
                            if packet_type == PacketType.E_S_ANS_USER_LIST:
                                print("사용자 목록 패킷 수신됨")
                                # 사용자 목록 파싱 (간단하게)
                                offset = 8  # 패킷 타입 다음부터
                                if len(decrypted_data) >= offset + 4:
                                    user_count = struct.unpack('<i', decrypted_data[offset:offset+4])[0]
                                    print(f"사용자 수: {user_count}")
                            elif packet_type == PacketType.E_S_ANS_NEW_USER_NOTIFY:
                                print("새 사용자 알림 패킷 수신됨")
                            else:
                                print(f"알 수 없는 패킷 타입: {packet_type}")
            else:
                print("응답 없음")
        except socket.timeout:
            print("응답 타임아웃")
        
        # 연결 종료
        sock.close()
        print("연결 종료")
        
    except Exception as e:
        print(f"오류 발생: {e}")
        if 'sock' in locals():
            sock.close()


if __name__ == "__main__":
    print("=== 간단한 채팅서버 연결 테스트 ===")
    simple_test()
