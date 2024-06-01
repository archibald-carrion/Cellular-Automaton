@echo off

REM Check if Python is installed
python --version >nul 2>&1

REM If the previous command failed, install Python
if errorlevel 1 (
    echo Python is not installed. Installing...
    
    REM Download Python installer
    powershell -Command "(New-Object Net.WebClient).DownloadFile('https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe', 'python-installer.exe')"
    
    REM Install Python
    start python-installer.exe /quiet PrependPath=1 Include_test=0

    REM Clean up installer
    del python-installer.exe
)

REM Check if customtkinter is installed
pip3 show customtkinter >nul 2>&1
if errorlevel 1 (
    echo customtkinter is not installed. Installing...
    pip3 install customtkinter
)

REM Check if psutil is installed
pip3 show psutil >nul 2>&1
if errorlevel 1 (
    echo psutil is not installed. Installing...
    pip3 install psutil
)

REM Run your Python app
python main.py