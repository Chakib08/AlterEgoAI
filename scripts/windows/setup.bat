@echo off
:: Script Name: setup.bat
:: Description: Setup pip env environment for development
:: Author: Mohamed Lamine KARTOBI
:: Date: 20/07/2025
:: Version: 1.0

set REQS_FILE=requirements.txt
set UTILS=scripts\windows\utils.bat

echo %UTILS%

:: Source external utilities (call the utils batch file)
call %UTILS%
if %errorlevel% neq 0 (
    call :print_err "Failed to source environment"
    exit /b 1
) else (
    call :print_success "Sourced environment successfully"
)

:: Check Python installation
call :print_info "Checking Python installation..."
python --version >nul 2>&1
if %errorlevel% neq 0 (
    call :print_err "Python is not installed or not found"
)
call :print_success "Python3 is installed."

:: Create and activate venv
call :print_info "Creating venv environment..."
python -m pip install --upgrade pip
python -m venv venv
call :activate_venv
if %errorlevel% neq 0 (
    call :print_err "Environment activation failed"
)
call :print_success "Environment was activated"

:: Upgrade pip3 to avoid requirements installation issues
pip install --upgrade pip

:: Install pip3 requirements
if exist %REQS_FILE% (
    call :print_info "Installing requirements..."
    pip install -r %REQS_FILE%
) else (
    call :print_warning "The requirements.txt file does not exist."
)

:: Deactivate the virtual environment
call :deactivate_venv
goto :eof

:: Functions

:: Print an info message
:print_info
echo [INFO] %1
goto :eof

:: Print a success message
:print_success
echo [SUCCESS] %1
goto :eof

:: Print an error message and exit
:print_err
echo [ERROR] %1
exit /b 1
goto :eof

:: Print a warning message
:print_warning
echo [WARNING] %1
goto :eof

:: Check if the virtual environment is activated, then activate it
:activate_venv
if exist venv\Scripts\activate (
    call venv\Scripts\activate.bat
) else (
    call :print_err "Virtual environment activation failed."
)
goto :eof

:: Deactivate virtual environment
:deactivate_venv
deactivate
goto :eof