@echo off
REM 서버 모니터링 도구 실행 스크립트

echo 서버 모니터링을 시작합니다...
echo.

REM Python 설치 확인
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo 오류: Python이 설치되어 있지 않습니다.
    echo Python 3.7 이상을 설치해주세요.
    pause
    exit /b 1
)

REM 서버 프로세스 확인
echo ChattingServer.exe 프로세스를 찾는 중...
tasklist /FI "IMAGENAME eq ChattingServer.exe" 2>NUL | find /I /N "ChattingServer.exe">NUL
if "%ERRORLEVEL%"=="0" (
    echo 서버 프로세스를 찾았습니다.
) else (
    echo 경고: ChattingServer.exe 프로세스를 찾을 수 없습니다.
    echo 서버가 실행 중인지 확인해주세요.
    echo.
)

REM 필요한 패키지 설치 확인
echo 필요한 패키지를 확인하고 설치합니다...
pip install -r requirements.txt

echo.
echo 서버 모니터링을 시작합니다.
echo Ctrl+C로 중지할 수 있습니다.
echo.

python server_monitor.py --process ChattingServer.exe --interval 1.0

pause
