@echo off
rem Set the name of the Python script
set PYTHON_SCRIPT=ufl_studio.py

rem Set the path to Python executable (update with actual path if necessary)
set PYTHON_PATH=C:\Users\isaac\AppData\Local\Programs\Python\Python312\python.exe

rem Set the path to the Python script (update with actual path if necessary)
set SCRIPT_PATH=C:\Users\isaac\Miscellanious\UFL\%PYTHON_SCRIPT%

rem Check if the Python script exists
if exist "%SCRIPT_PATH%" (
    echo Launching %PYTHON_SCRIPT%...
    "%PYTHON_PATH%" "%SCRIPT_PATH%"
) else (
    echo Error: %PYTHON_SCRIPT% not found at %SCRIPT_PATH%
)

pause
