# GameServer_Programming


## 서버 프로그램 구성
PC 클라이언트
    ├── 세션, 컨텐츠
    │     ├── DB
    │     ├── 로그
    │     │     ├── 서버

flowchart TD
    A[프로그램 시작] --> B[ID, PW 받기]
    B --> C[DB에 질의]
    C --> D{DB에 없는 ID 또는<br>잘못된 PW인가?}
    D -- Yes --> E[에러 처리<br>(에러 패킷 생성)]
    E --> F[클라이언트에 전송]
    F --> Z[끝]
    D -- No --> G{이 ID가 이미<br>접속중인가?}
    G -- Yes --> H[에러 패킷 생성]
    H --> I[클라이언트에 전송]
    I --> Z
    G -- No --> J[세션 객체 생성]
    J --> K[세션 객체를 pool에 등록]
    K --> Z


