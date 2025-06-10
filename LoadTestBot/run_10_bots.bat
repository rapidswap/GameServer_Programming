@echo off
chcp 65001 > nul
title 안전한 10개 봇 테스트

echo.
echo ==========================================
echo        🛡️ 안전한 10개 봇 테스트 🛡️  
echo ==========================================
echo.

:MENU
echo 테스트 옵션을 선택하세요:
echo.
echo [1] 무한 테스트 (수동 종료)
echo [2] 2분 테스트 (120초)
echo [3] 5분 테스트 (300초) 
echo [4] 10분 테스트 (600초)
echo [5] 사용자 정의 시간
echo [6] 실시간 모니터링 함께 실행
echo [7] 종료
echo.

set /p choice=선택 (1-7): 

if "%choice%"=="1" (
    echo.
    echo 🚀 무한 10개 봇 테스트를 시작합니다...
    echo 💡 중지하려면 Ctrl+C를 눌러주세요
    echo.
    python safe_10_test.py
    goto END
)

if "%choice%"=="2" (
    echo.
    echo 🚀 2분 10개 봇 테스트를 시작합니다...
    echo.
    python safe_10_test.py 120
    goto END
)

if "%choice%"=="3" (
    echo.
    echo 🚀 5분 10개 봇 테스트를 시작합니다...
    echo.
    python safe_10_test.py 300
    goto END
)

if "%choice%"=="4" (
    echo.
    echo 🚀 10분 10개 봇 테스트를 시작합니다...
    echo.
    python safe_10_test.py 600
    goto END
)

if "%choice%"=="5" (
    echo.
    set /p custom_time=테스트 시간을 초 단위로 입력하세요: 
    echo.
    echo 🚀 %custom_time%초 10개 봇 테스트를 시작합니다...
    echo.
    python safe_10_test.py %custom_time%
    goto END
)

if "%choice%"=="6" (
    echo.
    echo 🚀 실시간 모니터링과 함께 10개 봇 테스트를 시작합니다...
    echo 💡 두 개의 창이 열립니다:
    echo    - 모니터링 창: 서버 상태 실시간 확인
    echo    - 테스트 창: 10개 봇 테스트 실행
    echo.
    
    start "서버 모니터링" cmd /k "python realtime_monitor.py"
    timeout /t 3 >nul
    start "10개 봇 테스트" cmd /k "python safe_10_test.py 300"
    
    echo ✅ 모니터링과 테스트가 시작되었습니다!
    echo 💡 각 창에서 Ctrl+C로 종료할 수 있습니다.
    goto END
)

if "%choice%"=="7" (
    goto EXIT
)

echo ❌ 잘못된 선택입니다. 다시 선택해주세요.
echo.
goto MENU

:END
echo.
echo ✅ 10개 봇 테스트가 완료되었습니다!
echo.
echo 📊 결과 분석:
echo • 성공률 90%% 이상: 서버 안정성 우수
echo • 성공률 70-90%%: 서버 상태 양호  
echo • 성공률 70%% 미만: 서버 최적화 필요
echo.
pause

:EXIT
echo 👋 프로그램을 종료합니다.
