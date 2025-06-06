@echo off
REM 채팅서버 부하테스트 봇 실행 스크립트

echo 채팅서버 부하테스트 봇을 시작합니다...
echo.

REM Python 설치 확인
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo 오류: Python이 설치되어 있지 않습니다.
    echo Python 3.7 이상을 설치해주세요.
    pause
    exit /b 1
)

REM 필요한 패키지 설치 확인
echo 필요한 패키지를 확인하고 설치합니다...
pip install -r requirements.txt

echo.
echo 부하테스트 봇을 실행합니다.
echo 사용 가능한 명령어:
echo   start ^<봇수^> [테스트시간(초)] - 부하테스트 시작
echo   stop                          - 부하테스트 중지  
echo   stats                         - 현재 통계 표시
echo   broadcast ^<메시지^>            - 모든 봇에게 메시지 전송
echo   quit                          - 프로그램 종료
echo.

python main.py --interactive

pause
