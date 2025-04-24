# GameServer_Programming



# 로그인 서버, DBAgent, 채팅서버 & 클라이언트

이 프로젝트는 **동적 라이브러리(Server Library)** 기반의 서버를 이용해, 클라이언트의 로그인 및 채팅 기능을 제공하는 시스템입니다. 서버는 다중 스레드, IOCP 기반 네트워크 구조와 모듈화된 패킷/데이터베이스 처리를 통해 높은 확장성과 안정성을 목표로 설계되었습니다.

**아래 포함된 도서들을 기준으로 작성된 코드들이며 직접적으로 개발한 내용(‼️)은 유저입장, 유저목록, 유저퇴장 패킷, 브로드캐스트를 집중적으로 개발하여 채팅서버, 클라이언트의 내용을 더 풍부하게 만들었으며 후에 더 많은 기능들을 추가적으로 넣을 계획입니다.**

**[실행 영상](https://youtu.be/xjJY5UGZkzM)**

---

## 주요 구성 요소

### 1. 서버 라이브러리

- **Util**  
  - 메모리 관리, 애플리케이션 기본 처리, 쓰레드 관리, 로그 처리, 자료구조, 데이터 파서 등 기본 기능 제공

- **Type**  
  - 서버에서 사용될 타입들을 선언

- **Singleton**  
  - 단일 인스턴스 패턴을 통해 자원을 효율적으로 관리

- **Clock**  
  - 간단한 `chrono` 기반 시간 등록 라이브러리

- **ThreadJobQueue**  
  - 여러 쓰레드에서 실행되는 작업을 취합하여 결과를 관리

- **네트워크 구조 (IOCP)**  
  - 고성능 비동기 입출력 처리를 위한 IOCP 기반의 네트워크 처리

- **Server 클래스**  
  - 클라이언트 접속을 받아 세션을 생성 및 관리  
  - 클라이언트로부터 패킷 수신 및 처리 결과 전송  
  - 다른 서버와의 연결을 통해 서버 목록 관리

### 2. 세션 & 터미널

- **세션 클래스**  
  - 응용 프로세스가 통신을 관리할 수 있도록 클라이언트 소켓 정보를 보유  
  - 패킷 송수신 및 접속 종료 처리 담당

- **Terminal**  
  - 서버를 분할하여 모니터링  
  - 모든 플레이어가 동시에 튕기는 현상을 방지하기 위한 분산 관리

### 3. 패킷 처리

- **Encoder/Decoder**  
  - 콘텐츠 변경 시 일일이 수정할 필요 없이 자동으로 인코딩/디코딩 수행

- **Stream 클래스**  
  - 데이터를 순차적으로 넣고 빼는 직렬화 기능 제공

- **Packet 클래스**  
  - 패킷 종류를 나타내는 번호와 데이터 묶음을 직렬화

- **ContentsProcess**  
  - 들어온 데이터를 큐에 넣고, 등록된 함수 포인터 테이블(runFuncTable_)에 따라 각기 다른 처리 실행

### 4. 데이터베이스

- **DB 환경 구성**  
  - Hyper-V 기반 가상머신에 MS-SQL 및 ADODB를 설치하여 데이터베이스 운영  
  - 계정 및 플레이어 정보를 저장하는 테이블 구성

- **Stored Procedures**  
  - `p_AccountData_Select`, `p_AccountData_Insert`, `p_Character_Select`, `p_Character_Insert`  
  - QueryStatement 클래스를 통해 프로시저에 파라미터를 부착하여 쿼리 실행

- **QueryRecord**  
  - 로그인 처리를 위해 유저 정보를 전달하는 객체 역할

- **Database 클래스**  
  - 전체 데이터베이스를 총괄하여 관리

### 5. 로그인 서버 & DBAgent

‼️**주요 변경점:** 로그인에서의 비정상 혹은 정상 종료시 이루어지는 컨텐츠가 없어서 로그인 클라이언트에서 ContentsProcess 부분에서 퇴장시 부분을 더욱 명확하게 변경. 회원가입 기능을 넣어 새로운 유저가 들어왔을때 데이터베이스 관리를 설정함.

- **로그인 처리 흐름**  
  - **C_REQ_ID_PW:** 클라이언트가 ID/PW 전송
  - **I_DB_ANS_ID_PW:** DB에서 ID/PW 검증 후 성공/실패 응답
  - ‼️**C_REQ_CREATE_USER:** 클라이언트에서 새롭게 생성할 User의 ID와 PW를 DB서버에 전달
  - ‼️**I_DB_ANS_CREATE_USER:** DB서버에서 실행된 프로시저의 완료/실패 정보
  - ‼️**C_REQ_CREATE_CHARACTER_ID_PW:** 클라이언트에서 캐릭터를 생성하기 위해 ID와PW 먼저 검증
  - ‼️**I_DB_ANS_CREATE_CHARACTER:** DB서버에서 검증이 완료된 User의 캐릭터의 정보를 DB에 전달
  - ‼️**I_DB_ANS_CREATE_CHARACTER_SUCCESS:** DB서버에서 실행된 프로시저의 완료/실패 정보
  - **I_LOGIN_NOTIFY_ID_LOADED:** 로그인 성공 시, 해당 정보를 채팅서버에 전달
 

- **DBAgent**  
  - **I_DB_REQ_ID_PW:** 클라이언트의 ID와 비밀번호 요청 처리  
  - **I_DB_REQ_LOAD_DATA:** 요청 패킷에서 클라이언트 ID와 계정 ID 추출 후, 쿼리 생성 및 DB 매니저에 등록
  - ‼️**I_DB_REQ_CREATE_USER, I_DB_REQ_CREATE_CHARACTER_ID_PW, I_DB_REQ_CREATE_CHARACTER:** 클라이언트의 ID와 비밀번호 요청 처리, 유저의 캐릭터 정보를 정상적으로 저장했음을 알림 

### 6. 채팅 서버

‼️**주요 변경점:** 클라이언트 비정상 혹은 정상 종료시에 이루어지는 컨텐츠가 없어서 채팅 클라이언트에서 ContentsProcess 부분에서 퇴장시 부분을 더욱 명확하게 변경, UserManager에서 특정 ID(oid_t id)를 가진 유저 객체를 찾는 함수를 unordered_map, lower_bound(error 발생)를 사용하지 않고 map을 사용하는 방법으로 변경(map, find() 사용시 정확한 키 일치 보장). 

- **I_CHTTING_NOTIFY_ID:**  
  - 클라이언트의 채팅 알림 수신 후, DB 요청 패킷 생성 및 DBAgent에 전송

- **I_DB_ANS_PARSE_DATA:**  
  - DB 응답을 받아 클라이언트에게 로그인 성공 여부와 이름 전달

- **C_REQ_REGIST_CHATTING_NAME:**  
  - 클라이언트가 채팅 이름 등록 시 호출  
  - 이미 등록된 사용자인 경우 세션 종료, 신규 사용자 등록 후 사용자 목록 전송

- **C_REQ_CHATTING:**  
  - 등록된 사용자만 채팅 메시지를 전송 가능  
  - 메시지 전송 후 모든 사용자에게 브로드캐스트
  - 
- ‼️**E_S_ANS_NEW_USER_NOTIFY:**
  - 등록된 사용자가 로그인이 허용되었을 때 호출
  - 패킷 전송 후 메시지를 모든 유저에게 전송

- ‼️**E_S_ANS_USER_LIST:**
  - 로그인이 허용되었을 시점에서 유저리스트를 불러오도록 패킷 전송
    
- ‼️**C_REQ_CHAT_EXIT:**  
  - 채팅 종료 요청 시, 등록 여부에 따라 세션 종료 또는 사용자 목록에서 제거 후 브로드캐스트

---

## 로그인 프로세스 다이어그램

아래 다이어그램은 로그인 프로세스의 흐름을 시각적으로 표현한 것입니다.

flowchart TD
    A[프로그램 시작] --> B[ID, PW 받기]
    
    B --> C[DB에 질의]
    
    C --> D{DB에 없는 ID<br>또는 잘못된 PW인가?}
    
    D -- Yes --> E[에러 처리<br>(에러 패킷 생성)]
    
    E --> F[클라이언트에 전송]
    
    F --> Z[종료]
    
    D -- No --> G{이미 접속중인가?}
    
    G -- Yes --> H[에러 패킷 생성]
    
    H --> I[클라이언트에 전송]
    
    I --> Z
    
    G -- No --> J[세션 객체 생성]
    
    J --> K[세션 객체를 pool에 등록]
    
    K --> Z
    

## 시퀀스 다이어그램
![Image](https://github.com/user-attachments/assets/84176ed8-2006-499d-9302-837f73633e88)

## 회원가입 시퀀스 다이어그램
![Image](https://github.com/user-attachments/assets/2f9349f9-5300-4f28-8547-cab807f13459)
## 마무리
이 시스템은 모듈화된 서버 라이브러리와 효율적인 패킷/데이터베이스 처리, 그리고 다수의 클라이언트를 동시에 지원하는 네트워크 구조를 통해 높은 확장성과 안정성을 제공합니다. 각 모듈은 독립적으로 관리되며, 필요에 따라 손쉽게 기능 확장이 가능하도록 설계되었습니다.

## 참고자료
[게임 서버 프로그래밍 입문](https://product.kyobobook.co.kr/detail/S000060600761)

[윤성우 열혈 TCP/IP 소켓 프로그래밍](https://product.kyobobook.co.kr/detail/S000001589146)

[게임 서버 프로그래밍 교과서](https://product.kyobobook.co.kr/detail/S000001792817)
