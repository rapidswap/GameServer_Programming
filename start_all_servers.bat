@echo off
title Game Server Launcher
echo ==========================================
echo        게임 서버 통합 런처
echo ==========================================
echo.

echo [1단계] DBAgent 서버 시작 중...
cd /d "C:\github\GameServer_Programming\ServerLibrary\x64\Debug"
start "DBAgent" DBAgent.exe
timeout /t 3

echo [2단계] LoginServer 서버 시작 중...
start "LoginServer" LoginServer.exe
timeout /t 3

echo [3단계] ChattingServer 서버 시작 중...
start "ChattingServer" ChattingServer.exe
timeout /t 2

echo.
echo ==========================================
echo 모든 서버가 시작되었습니다!
echo.
echo 실행 중인 서버들:
echo - DBAgent (포트 9300)
echo - LoginServer (포트 9000) 
echo - ChattingServer (포트 9200)
echo.
echo 클라이언트 접속 주소: 127.0.0.1:9000
echo ==========================================
pause