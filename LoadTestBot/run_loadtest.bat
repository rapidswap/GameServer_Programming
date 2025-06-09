@echo off
chcp 65001 >nul
REM Chat Server Load Test Bot

echo Starting Chat Server Load Test Bot...
echo.

REM Check Python installation
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed.
    echo Please install Python 3.7 or higher.
    pause
    exit /b 1
)

REM Install required packages
echo Checking and installing required packages...
pip install -r requirements.txt

echo.
echo Load Test Bot is starting.
echo Available commands:
echo   start ^<bots^> [duration] - Start load test
echo   stop                      - Stop load test  
echo   stats                     - Show current stats
echo   broadcast ^<message^>      - Send message to all bots
echo   quit                      - Exit program
echo.

python main.py --interactive

pause
