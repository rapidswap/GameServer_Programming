@echo off
chcp 65001 >nul
REM Server Monitoring Tool

echo Starting Server Monitoring...
echo.

REM Check Python installation
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed.
    echo Please install Python 3.7 or higher.
    pause
    exit /b 1
)

REM Check server process
echo Looking for ChattingServer.exe process...
tasklist /FI "IMAGENAME eq ChattingServer.exe" 2>NUL | find /I /N "ChattingServer.exe">NUL
if "%ERRORLEVEL%"=="0" (
    echo Server process found.
) else (
    echo Warning: ChattingServer.exe process not found.
    echo Please make sure the server is running.
    echo.
)

REM Install required packages
echo Checking and installing required packages...
pip install -r requirements.txt

echo.
echo Starting server monitoring.
echo Press Ctrl+C to stop.
echo.

python server_monitor.py --process ChattingServer.exe --interval 1.0

pause
