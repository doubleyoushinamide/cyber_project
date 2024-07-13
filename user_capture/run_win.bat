@echo off
setlocal enabledelayedexpansion

REM or remark: - path to your Git Bash installation
REM If you installed Git properlly by default your path should be at `C:\Program Files\Git\bin\bash.exe`
set GIT_BASH_PATH = C:\Program Files\Git\bin\bash.exe

REM chanell the path to our capture_users.sh
set SCRIPT_PATH=%~dp0capture_users.sh

"%GIT_BASH_PATH%" --login -i -c "bash '%SCRIPT_PATH%'"

REM This only works if you have arp-scan installed on your windows