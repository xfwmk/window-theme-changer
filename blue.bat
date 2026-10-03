@echo off
python blue.py
REM python testblue.py
timeout /t 2 /nobreak >nul
cls
cd C:\Users\opel\.vscode
python run.py
cd C:\Users\opel