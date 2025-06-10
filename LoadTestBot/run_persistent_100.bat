@echo off
chcp 65001 > nul
title 100개 봇 지속 대화 테스트

echo.
echo ==========================================
echo     🤖💬 100개 봇 지속 대화 테스트 💬🤖
echo ==========================================
echo.

echo ⚠️  주의사항:
echo • 이 테스트는 100개 봇이 계속 대화합니다
echo • 서버에 지속적인 부하가 가해집니다
echo • 종료하려면 Ctrl+C를 눌러주세요
echo • 서버가 실행 중이어야 합니다
echo.

:MENU
echo 실행 옵션을 선택하세요:
echo.
echo [1] 100개 봇 지속 대화 시작
echo [2] 모니터링과 함께 실행
echo [3] 서버 상태 확인 (연결 테스트)
echo [4] 사용법 및 도움말
echo [5] 종료
echo.

set /p choice=선택 (1-5): 

if "%choice%"=="1" (
    echo.
    echo 🚀 100개 봇 지속 대화를 시작합니다...
    echo 💡 이 테스트는 무한히 실행됩니다 (Ctrl+C로 종료)
    echo.
    python persistent_100_chat.py
    goto END
)

if "%choice%"=="2" (
    echo.
    echo 🚀 모니터링과 함께 100개 봇 대화를 시작합니다...
    echo 💡 두 개의 창이 열립니다:
    echo    - 모니터링 창: 서버 상태 실시간 확인
    echo    - 대화 창: 100개 봇 지속 대화
    echo.
    
    start "실시간 서버 모니터링" cmd /k "python realtime_monitor.py"
    timeout /t 3 >nul
    start "100개 봇 지속 대화" cmd /k "python persistent_100_chat.py"
    
    echo ✅ 모니터링과 대화가 시작되었습니다!
    echo 💡 각 창에서 Ctrl+C로 종료할 수 있습니다.
    goto END
)

if "%choice%"=="3" (
    echo.
    echo 🔍 서버 연결 상태를 확인합니다...
    echo 💡 단일 봇으로 서버 기본 연결을 테스트합니다.
    echo.
    python single_bot_test.py 30
    echo.
    echo 서버 연결 테스트가 완료되었습니다.
    echo 연결이 성공했다면 100개 봇 테스트를 진행하세요.
    echo.
    pause
    goto MENU
)

if "%choice%"=="4" (
    echo.
    echo ==========================================
    echo           📚 사용법 및 도움말
    echo ==========================================
    echo.
    echo 🎯 목적:
    echo • 100개 봇이 자연스러운 대화를 지속
    echo • 서버의 장시간 안정성 테스트
    echo • 실제 사용자 환경 시뮬레이션
    echo.
    echo 🤖 봇 특징:
    echo • 5가지 개성: 친근한, 게이머, 관찰자, 응원단, 테스터
    echo • 8가지 대화 주제: 인사, 게임, 일상, 날씨, 응원, 생각, 반응, 테스트
    echo • 5-25초 간격으로 개성에 맞는 메시지 전송
    echo • 각 봇마다 고유한 대화 패턴
    echo.
    echo 📊 모니터링:
    echo • 30초마다 기본 통계 출력
    echo • 2분마다 상세 통계 출력
    echo • 실시간 연결 상태 확인
    echo • 메시지 처리량 및 응답시간 측정
    echo.
    echo 🛑 종료 방법:
    echo • Ctrl+C: 안전한 종료
    echo • 모든 봇이 순차적으로 연결 해제됨
    echo • 최종 통계 및 결과 출력
    echo.
    echo ⚠️  주의사항:
    echo • 서버가 실행 중이어야 함
    echo • 지속적인 서버 부하 발생
    echo • 충분한 시스템 리소스 필요
    echo ==========================================
    echo.
    pause
    goto MENU
)

if "%choice%"=="5" (
    goto EXIT
)

echo ❌ 잘못된 선택입니다. 다시 선택해주세요.
echo.
goto MENU

:END
echo.
echo ✅ 100개 봇 지속 대화가 완료되었습니다!
echo.
echo 📊 결과 요약:
echo • 대화 시간 및 메시지 수 확인
echo • 서버 안정성 평가
echo • 상세 로그는 JSON 파일에 저장됨
echo.
echo 💡 서버 성능 분석:
echo • 연결 유지율 90%% 이상: 우수
echo • 평균 응답시간 100ms 미만: 양호
echo • 오류 발생률 5%% 미만: 안정적
echo.
pause

:EXIT
echo.
echo 👋 100개 봇 지속 대화 테스트를 종료합니다.
echo 감사합니다!
