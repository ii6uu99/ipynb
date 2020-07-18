@echo off

REM SETUP Python Virtual Environment ('venv'), activate it, and upgrade pip in with one command

REM DIRECT SCRIPT BASED ON PARAMETER
IF %1.==. GOTO ActivateCreate
IF %1==help GOTO HelpText
IF %1==delete GOTO Delete


:HelpText
echo ARGUMENTS
echo [empty] - if 'venv' exists, activate, if not, create, activate, and setup
echo  delete - delete Python Virtual Environment ('venv' folder)
GOTO :End1


:ActivateCreate
IF EXIST %cd%\venv\. ( 
   venv\scripts\activate
) ELSE ( 
    echo STEP 1: Create Python Virtual Environment
    python -m venv venv
    echo STEP 2: Activate Virtual Enviroment
    venv\scripts\activate
    echo STEP 3: Upgrade Python PIP
    python -m pip install --upgrade pip
    echo COMPLETE: Python Virtual Enviroment
    IF EXIST requirements.txt ( python -m pip install -r requirements.txt )
)


:Delete
IF %1==delete ( rmdir /s /q venv && echo Python Virtual Environment 'venv' Removed )
GOTO :End1

:End1

REM NOTES IF THEY ARE NEEDED (DOESN'T RUN FILE)
REM set parameters
REM set arg1=%1