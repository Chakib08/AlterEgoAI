@echo off
:: Script Name: utils.bat
:: Description: Include function for logs
:: Author: Mohamed Lamine KARTOBI
:: Date: 17/01/2025
:: Version: 1.0

:: === COLORS ===
set RED=^[[31m
set GREEN=^[[32m
set YELLOW=^[[33m
set CYAN=^[[36m
set RESET=^[[0m

:: === FUNCTIONS ===
call :print_info "Info: Utility script started."

:: Print an info message
:print_info
echo %CYAN%[INFO]%RESET% %1
goto :eof

:: Print a success message
:print_success
echo %GREEN%[SUCCESS]%RESET% %1
goto :eof

:: Print an error message and exit
:print_err
echo %RED%[ERROR]%RESET% %1
exit /b 1
goto :eof

:: Print a warning message
:print_warning
echo %YELLOW%[WARNING]%RESET% %1
goto :eof

:: Check for error (last exit code) and print error or success
:chkerr
if not %errorlevel%==0 (
    if not "%1"=="" (
        call :print_err "%1"
    ) else (
        call :print_err "failed."
    )
    exit /b 1
) else (
    if "%1"=="" (
        call :print_success "done."
    )
)
goto :eof