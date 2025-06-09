@echo off
chcp 65001 >nul
REM Progressive Load Test Script

echo Progressive Load Test starting...
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
echo Installing required packages...
pip install -r requirements.txt >nul 2>&1

echo.
echo Progressive Load Test Scenarios:
echo   1. Warm-up Test (1-10 bots, linear)
echo   2. Basic Load Test (5-50 bots, step)  
echo   3. Exponential Growth (1-64 bots)
echo   4. Spike Test (10-100 bots sudden)
echo   5. Ramp Up/Down (increase then decrease)
echo   6. Sustained Load (20 bots for 5min)
echo   7. Stress Test (increase to limit)
echo   8. Custom Test
echo   9. Adaptive Auto Test
echo.

set /p choice="Select scenario (1-9): "

if "%choice%"=="1" (
    echo Running Warm-up Test...
    python progressive_test.py --scenario 1
) else if "%choice%"=="2" (
    echo Running Basic Load Test...
    python progressive_test.py --scenario 2
) else if "%choice%"=="3" (
    echo Running Exponential Growth Test...
    python progressive_test.py --scenario 3
) else if "%choice%"=="4" (
    echo Running Spike Test...
    python progressive_test.py --scenario 4
) else if "%choice%"=="5" (
    echo Running Ramp Up/Down Test...
    python progressive_test.py --scenario 5
) else if "%choice%"=="6" (
    echo Running Sustained Load Test...
    python progressive_test.py --scenario 6
) else if "%choice%"=="7" (
    echo Running Stress Test...
    python progressive_test.py --scenario 7
) else if "%choice%"=="8" (
    echo Running Custom Test...
    python progressive_test.py --interactive
) else if "%choice%"=="9" (
    echo Running Adaptive Auto Test...
    set /p initial_bots="Initial bots (default: 5): "
    set /p max_bots="Max bots (default: 50): "
    if "%initial_bots%"=="" set initial_bots=5
    if "%max_bots%"=="" set max_bots=50
    python adaptive_load_tester.py --initial-bots %initial_bots% --max-bots %max_bots%
) else (
    echo Please select a valid number.
    pause
    exit /b 1
)

pause
