# 채팅서버 부하테스트 봇

Python으로 개발된 **고급 채팅서버 부하테스트 도구**입니다. 기본 부하테스트부터 점진적 부하 증가, 적응형 자동 테스트까지 지원합니다.

## 🚀 주요 기능

### 1. 기본 부하테스트
- 동시 다중 클라이언트 연결
- 자동 채팅 메시지 전송  
- 실시간 통계 및 모니터링
- 네트워크 지연시간 측정

### 2. **점진적 부하테스트 (NEW!)**
- **7가지 사전정의 시나리오**
- 선형/지수/단계적 증가 패턴
- 스파이크/램프업다운 테스트
- 스트레스 테스트 (한계점 탐지)

### 3. **적응형 자동 테스트 (NEW!)**  
- 실시간 성능 모니터링
- 자동 부하 조절 (CPU/메모리 기반)
- 최적 동접자 수 자동 탐지
- 성능 임계값 기반 스케일링

### 4. 서버 모니터링
- 서버 프로세스 리소스 사용량
- CPU, 메모리, 네트워크 추적
- 실시간 연결 수 모니터링

## 파일 구조

```
LoadTestBot/
├── main.py                      # 기본 부하테스트 실행기
├── progressive_test.py           # 점진적 부하테스트 실행기 ⭐
├── adaptive_load_tester.py       # 적응형 자동 테스트 ⭐
├── progressive_load_tester.py    # 점진적 테스트 매니저
├── load_test_manager.py         # 기본 부하테스트 매니저
├── chat_bot_client.py           # 개별 봇 클라이언트
├── packets.py                   # 패킷 클래스들
├── packet_util.py               # 패킷 유틸리티
├── packet_types.py              # 패킷 타입 정의
├── packet_obfuscation.py        # 패킷 암호화/복호화
├── server_monitor.py            # 서버 모니터링 도구
├── simple_test.py               # 간단한 연결 테스트
├── run_progressive_test.bat     # 점진적 테스트 실행 스크립트 ⭐
├── run_loadtest.bat             # 기본 부하테스트 실행
├── run_monitor.bat              # 서버 모니터링 실행
├── PROGRESSIVE_TEST_GUIDE.md    # 점진적 테스트 가이드 ⭐
├── requirements.txt             # 필요 패키지
└── README.md                    # 이 파일
```

## 🚀 빠른 시작

### ✨ **점진적 부하테스트 (추천)**
```bash
# 간단한 실행
run_progressive_test.bat

# 또는 직접 실행
python progressive_test.py --scenario 2  # 기본 부하테스트
```

### 필요 패키지 설치
```bash
pip install psutil
```

### 기본 실행 (대화형 모드)
```bash
python main.py
```

### 명령줄 옵션
```bash
python main.py --host localhost --port 9200 --interactive
```

### 배치 모드 실행
```bash
# 10개 봇으로 60초간 테스트
python main.py --bots 10 --duration 60 --output results.json

# 서버 주소 지정
python main.py --host 192.168.1.100 --port 9200 --bots 5 --duration 30
```

## 📈 점진적 부하테스트

### 사전 정의된 시나리오

| 번호 | 시나리오명 | 패턴 | 봇 수 | 설명 |
|------|------------|------|-------|------|
| 1 | 웜업 테스트 | 선형 | 1→10 | 기본 성능 파악 |
| 2 | 기본 부하테스트 | 단계 | 5→50 | 일반적인 부하테스트 |
| 3 | 지수적 증가 | 지수 | 1→64 | 빠른 한계점 탐지 |
| 4 | 스파이크 테스트 | 급증 | 10→100 | 순간 부하 대응능력 |
| 5 | 램프업/다운 | 증감 | 5→40→5 | 부하 변화 적응성 |
| 6 | 지속적 부하 | 지속 | 20개 | 안정성 테스트 |
| 7 | 스트레스 테스트 | 한계 | 10→200 | 최대 처리량 탐지 |

### 실행 방법

#### A. 간단한 실행
```bash
# 배치 스크립트 실행
run_progressive_test.bat

# 또는 직접 실행
python progressive_test.py --scenario 2
```

#### B. 명령줄 실행
```bash
# 기본 부하테스트 (5→50 봇, 5개씩 증가)
python progressive_test.py --scenario 2

# 사용자 정의 테스트
python progressive_test.py --start-bots 1 --max-bots 30 --step-size 3 --step-duration 45

# 적응형 자동 테스트
python adaptive_load_tester.py --initial-bots 5 --max-bots 100
```

#### C. 대화형 모드
```bash
python progressive_test.py --interactive

# 사용 가능한 명령어:
# list     - 시나리오 목록
# run 2    - 2번 시나리오 실행  
# custom   - 사용자 정의 시나리오
# status   - 현재 상태
# report   - 진행 상황 리포트
# export   - 결과 내보내기
# stop     - 테스트 중지
```

## 🤖 적응형 자동 테스트

서버 성능을 실시간으로 모니터링하며 자동으로 부하를 조절하는 고급 기능입니다.

### 주요 특징
- **실시간 성능 모니터링**: CPU, 메모리, 응답시간, 성공률
- **자동 스케일링**: 성능 임계값 기반 봇 수 자동 조절
- **최적점 탐지**: 최대 안정 동접자 수 자동 발견
- **스마트 알고리즘**: 30초 안정 후 증가, 즉시 감소

### 성능 임계값
```python
CPU 사용률: 80% 이하
메모리 사용률: 85% 이하  
응답시간: 1000ms 이하
성공률: 95% 이상
오류율: 5% 이하
```

### 실행 방법
```bash
# 기본 실행
python adaptive_load_tester.py

# 상세 설정
python adaptive_load_tester.py --initial-bots 10 --max-bots 200 --duration 1800
```

## 📊 결과 예시

### 점진적 부하테스트 결과
```
단계 1: 5개 봇
  연결된 봇: 5/5
  메시지: 전송 45, 수신 225
  오류: 0
  처리량: 0.8 메시지/초

단계 2: 10개 봇
  연결된 봇: 10/10
  메시지: 전송 89, 수신 890
  오류: 0
  처리량: 1.5 메시지/초

단계 3: 15개 봇 (성능 저하 시작)
  연결된 봇: 14/15
  메시지: 전송 125, 수신 1680
  오류: 1
  처리량: 2.1 메시지/초
```

### 적응형 테스트 결과
```
🔄 새 단계 시작: 5개 봇으로 30초간 테스트
🔄 봇 수 증가: 5 → 6 (성능 양호)
🔄 봇 수 증가: 6 → 7
🔄 봇 수 증가: 7 → 8
⚠️  성능 저하 감지! CPU 85% 도달
🔄 봇 수 감소: 8 → 6 (성능 안정화)

최대 안정 봇 수: 7개
```

## 🚀 추천 사용 시나리오

### 1단계: 초기 테스트
```bash
# 웜업 테스트로 기본 성능 파악
python progressive_test.py --scenario 1
```

### 2단계: 일반 부하테스트
```bash
# 기본 부하테스트로 주요 성능 지표 파악
python progressive_test.py --scenario 2
```

### 3단계: 한계점 탐지
```bash
# 스트레스 테스트로 최대 처리량 파악
python progressive_test.py --scenario 7
```

### 4단계: 최적화
```bash
# 적응형 테스트로 최적 동접자 수 탐지
python adaptive_load_tester.py --max-bots 50
```

## 🛠️ 고급 기능

### 다중 서버 테스트
```bash
# 여러 서버 동시 테스트
python progressive_test.py --host server1 --scenario 2 &
python progressive_test.py --host server2 --scenario 2 &
```

### 서버 모니터링 동시 실행
```bash
# 터미널 1: 서버 모니터링
python server_monitor.py --output monitoring.json

# 터미널 2: 부하테스트
python progressive_test.py --scenario 2 --output loadtest.json
```

### 사용자 정의 패턴
```bash
# 사용자 정의 시나리오
python progressive_test.py \
  --start-bots 2 \
  --max-bots 25 \
  --step-size 3 \
  --step-duration 40 \
  --output custom_test.json
```

## 📝 주요 특징

### 봇 클라이언트
- 자동 이름 등록
- 랜덤 채팅 메시지 전송 (3-8초 간격)
- 주기적 핑 테스트 (30초 간격)
- 연결 재시도 로직
- 통계 수집 및 보고

### 테스트 매니저
- 다중 봇 생성 및 관리
- 점진적 연결 (서버 부하 방지)
- 실시간 통계 모니터링
- JSON 형태 결과 내보내기
- 브로드캐스트 메시지 기능

### 서버 모니터링
- 프로세스별 리소스 사용량 추적
- 시스템 전체 성능 모니터링
- 네트워크 I/O 통계
- 연결 수 실시간 추적

## 📋 비교 분석

| 기능 | 기본 봄하테스트 | 점진적 테스트 | 적응형 테스트 |
|------|-------------|-------------|-------------|
| **난이도** | ⭐ 기초 | ⭐⭐ 중급 | ⭐⭐⭐ 고급 |
| **설정** | 간단 | 시나리오 선택 | 임계값 설정 |
| **사용 목적** | 기본 성능 파악 | 한계점 탐지 | 최적점 찾기 |
| **결과 분석** | 단순 통계 | 단계별 성능 | 실시간 최적화 |
| **추천 상황** | 초보자 | 일반 테스터 | 전문가/운영팀 |

## 🔧 문제 해결

### 연결 실패 시
1. 서버 상태 확인: `netstat -an | findstr :9200`
2. 방화벽 설정 검토
3. 동시 연결 수 제한 확인
4. 서버 로그 분석

### 성능 이상 시
1. 시스템 리소스 모니터링: `python server_monitor.py`
2. 네트워크 상태 점검
3. 데이터베이스 성능 확인
4. 서버 프로세스 로그 분석

### 테스트 결과 활용
1. **용량 계획**: 최대 처리량 기반 서버 규모 결정
2. **알람 설정**: 성능 임계값 기반 모니터링 구성
3. **오토스케일링**: 부하 패턴 기반 자동 확장 설정
4. **성능 최적화**: 병목 구간 개선 우선순위 결정

---

## 🏆 결론

이 부하테스트 도구로 **서버의 진짜 성능과 한계점을 정확히 파악**할 수 있습니다. 기본 테스트부터 고급 적응형 테스트까지, 여러분의 요구사항에 맞는 테스트 전략을 선택하여 사용하세요.

### **추천 시작 방법**
```bash
# 1. 간단한 시작
run_progressive_test.bat

# 2. 웜업 테스트 선택 (1번)
# 3. 결과 확인 후 계속 진행
# 4. 다양한 시나리오 체험
```

**이제 체계적이고 전문적인 부하테스트로 서버의 진짜 성능을 확인해보세요!** 🚀

1. **start <봇수> [테스트시간(초)]** - 부하테스트 시작
   ```
   start 10        # 10개 봇으로 무제한 테스트
   start 20 300    # 20개 봇으로 300초간 테스트
   ```

2. **stop** - 부하테스트 중지
   ```
   stop
   ```

3. **stats** - 현재 통계 표시
   ```
   stats
   ```

4. **export [파일명]** - 통계 JSON 파일로 내보내기
   ```
   export              # 자동 파일명
   export my_test.json # 지정된 파일명
   ```

5. **broadcast <메시지>** - 모든 봇에게 메시지 전송
   ```
   broadcast 안녕하세요 모든 봇들!
   ```

6. **quit** - 프로그램 종료
   ```
   quit
   ```

### 서버 모니터링 실행

```bash
# 기본 모니터링
python server_monitor.py

# 특정 프로세스 모니터링
python server_monitor.py --process ChattingServer.exe --interval 2.0

# 300초간 모니터링 후 결과 저장
python server_monitor.py --duration 300 --output server_stats.json
```

## 테스트 시나리오 예시

### 1. 기본 부하테스트
```bash
# 10개 봇으로 5분간 테스트
python main.py --bots 10 --duration 300
```

### 2. 점진적 부하 증가 테스트
```bash
# 대화형 모드에서 순차적으로 실행
start 5      # 5개 봇으로 시작
# 잠시 후
stop
start 10     # 10개 봇으로 증가
# 잠시 후
stop
start 20     # 20개 봇으로 증가
```

### 3. 서버 모니터링과 함께 테스트
```bash
# 터미널 1: 서버 모니터링
python server_monitor.py --output monitoring.json

# 터미널 2: 부하테스트
python main.py --bots 15 --duration 600 --output loadtest.json
```

## 출력 예시

### 부하테스트 통계
```
================================================================================
부하테스트 상태 - 2025-06-06 14:30:15
================================================================================
테스트 시간: 125.3초
봇 상태: 10/10 연결됨
메시지: 전송 156, 수신 1520
오류 수: 0
레이턴시: 평균 23.4ms, 최소 12ms, 최대 45ms
처리량: 1.2 메시지/초
```

### 서버 모니터링
```
서버 모니터링 - 2025-06-06T14:30:15 (경과: 125.3초)
======================================================================
시스템 CPU: 15.2%
시스템 메모리: 68.4% (5.5GB/8.0GB)
서버 프로세스 CPU: 12.5%, 연결: 10개
```
