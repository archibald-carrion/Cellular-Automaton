@echo off

REM Check if Python is installed
python --version >nul 2>&1

REM If the previous command failed, install Python
if errorlevel 1 (
    echo Python is not installed. Installing...
    
    REM Download Python installer
    powershell -Command "(New-Object Net.WebClient).DownloadFile('https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe', 'python-installer.exe')"
    
    REM Install Python
    start /wait python-installer.exe /quiet PrependPath=1 Include_test=0

    REM Clean up installer
    del python-installer.exe
)

pip3 show pygame >nul 2>&1
if errorlevel 1 (
    echo pygame is not installed. Installing...
    pip3 install pygame
)

REM Run your Python app with the determined parameter
python main.py
