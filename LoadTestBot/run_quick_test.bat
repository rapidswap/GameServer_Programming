@echo off
chcp 65001 >nul
REM Quick Test Script

echo Quick Connection Test
echo =====================

REM Check Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python not found. Please install Python 3.7+
    pause
    exit /b 1
)

REM Install packages if needed
if not exist "requirements.txt" (
    echo requirements.txt not found. Creating...
    echo psutil>=5.8.0 > requirements.txt
)

pip install -r requirements.txt >nul 2>&1

echo.
echo Testing connection to chat server...
echo Server: localhost:9200
echo.

python simple_test.py

echo.
echo Test completed. Check the results above.
pause
