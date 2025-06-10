@echo off
chcp 65001 > nul
title 100개 봇 동시 접속 테스트

echo.
echo ==========================================
echo        🤖 100개 봇 테스트 실행기 🤖  
echo ==========================================
echo.

:MENU
echo 테스트 옵션을 선택하세요:
echo.
echo [1] 무한 테스트 (수동 종료)
echo [2] 5분 테스트 (300초)
echo [3] 10분 테스트 (600초) 
echo [4] 30분 테스트 (1800초)
echo [5] 사용자 정의 시간
echo [6] 종료
echo.

set /p choice=선택 (1-6): 

if "%choice%"=="1" (
    echo.
    echo 🚀 무한 테스트를 시작합니다...
    echo 💡 중지하려면 Ctrl+C를 눌러주세요
    echo.
    python test_100_bots.py
    goto END
)

if "%choice%"=="2" (
    echo.
    echo 🚀 5분 테스트를 시작합니다...
    echo.
    python test_100_bots.py 300
    goto END
)

if "%choice%"=="3" (
    echo.
    echo 🚀 10분 테스트를 시작합니다...
    echo.
    python test_100_bots.py 600
    goto END
)

if "%choice%"=="4" (
    echo.
    echo 🚀 30분 테스트를 시작합니다...
    echo.
    python test_100_bots.py 1800
    goto END
)

if "%choice%"=="5" (
    echo.
    set /p custom_time=테스트 시간을 초 단위로 입력하세요: 
    echo.
    echo 🚀 %custom_time%초 테스트를 시작합니다...
    echo.
    python test_100_bots.py %custom_time%
    goto END
)

if "%choice%"=="6" (
    goto EXIT
)

echo ❌ 잘못된 선택입니다. 다시 선택해주세요.
echo.
goto MENU

:END
echo.
echo ✅ 테스트가 완료되었습니다!
echo.
pause

:EXIT
echo 👋 프로그램을 종료합니다.
