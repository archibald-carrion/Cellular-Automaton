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

REM Check if the necessary packages are installed
pip3 show customtkinter >nul 2>&1
if errorlevel 1 (
    echo customtkinter is not installed. Installing...
    pip3 install customtkinter
)

pip3 show psutil >nul 2>&1
if errorlevel 1 (
    echo psutil is not installed. Installing...
    pip3 install psutil
)

pip3 show pygame >nul 2>&1
if errorlevel 1 (
    echo pygame is not installed. Installing...
    pip3 install pygame
)

pip3 show tkinter >nul 2>&1
if errorlevel 1 (
    echo tkinter is not installed. Installing...
    pip3 install tkinter
)

REM Determine which argument was provided and set the corresponding parameter
set param=customtkinter
if "%1"=="" (
    echo No argument provided. Using default: customtkinter
) else (
    if "%1"=="pygame" (
        set param=pygame
    ) else if "%1"=="tkinter" (
        set param=tkinter
    ) else if "%1"=="customtkinter" (
        set param=customtkinter
    ) else (
        echo Invalid argument provided. Using default: customtkinter
    )
)

REM Run your Python app with the determined parameter
python main.py %param%
