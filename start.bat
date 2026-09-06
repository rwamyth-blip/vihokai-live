@echo off
title ViHok AI - www.vihokai.com - Start Both
color 0A
echo ================================================
echo  ViHok AI - vihokai.com - เหนือชั้นแบบนก
echo  Starting Frontend + Backend...
echo ================================================
echo.

REM Go to project root
cd /d "%~dp0"

if not exist "ai_super_platform" (
  echo ERROR: Please put start.bat inside vihokai_com_complete folder
  echo Current: %CD%
  pause
  exit /b
)

echo [1/4] Checking Backend venv...
cd ai_super_platform\backend
if not exist venv (
    echo   - Creating venv...
    py -m venv venv
)
echo   - Activating venv and installing libs...
call venv\Scripts\activate.bat
pip install --upgrade pip -q
if exist requirements.txt (
    pip install -r requirements.txt -q
) else (
    pip install fastapi uvicorn[standard] openai groq google-generativeai python-dotenv pydantic httpx -q
)
cd ..\..

echo [2/4] Checking Frontend...
cd ai_super_platform\frontend
if not exist node_modules (
    echo   - Installing npm packages (first time may take 2-3 min)...
    call npm install
)
cd ..\..

echo [3/4] Starting Backend on http://localhost:8000 ...
start "ViHok Backend - api.vihokai.com" cmd /k "cd /d %~dp0ai_super_platform\backend && call venv\Scripts\activate.bat && echo Backend running at http://localhost:8000/docs && uvicorn main:app --reload --port 8000"

echo [4/4] Starting Frontend on http://localhost:3000 ...
timeout /t 3 /nobreak >nul
start "ViHok Frontend - www.vihokai.com" cmd /k "cd /d %~dp0ai_super_platform\frontend && echo Frontend running at http://localhost:3000 && npm run dev"

echo.
echo ================================================
echo  DONE! Both running
echo  Frontend: http://localhost:3000
echo  Backend : http://localhost:8000/docs
echo  Close this window to keep servers running in background
echo  Or press any key to open browser
echo ================================================
pause
start http://localhost:3000
start http://localhost:8000/docs
