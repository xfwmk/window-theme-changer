@echo off
python green.py
REM python testgreen.py
timeout /t 2 /nobreak >nul
cls
cd C:\Users\opel\.vscode
python run.py
cd C:\Users\opel