@echo off
REM This script launches the given Python script from the given directory

REM Chris Nyland
REM 2015-12-09
REM Last Updated: 2017-10-19

REM This script launches the given Python script taking into account several
REM situations. There are a total of three arguments that can be given.
REM The first is the full path to the directory where the script in question
REM resides. The second argument is the name of the script it self. The
REM third argument is optional and effects the way the script is launched.
REM Specifically there are two different ways to start the script in PDB
REM debugger mode and starting it in and IPython interactive session.
REM This script also searches for the existence of a virtual environment and
REM if found activates it and runs the script using the virtual environment.
REM The virtual environment is found by searching for a specified folder name
REM defined by the "virtualfolder" variable in the script below.
REM The Python installation to start the script with is determined by using the
REM Py Launcher program and the shebang line in the script file. If no
REM shebang line is present then the default Python installation found by
REM PyLauncher.
REM This will fail badly if the line endings are not Windows

REM Give the window a unique title
title PyLauncher Running %1 %2

REM Setup most of the variables that we need for the script
set virtualfolder=venv
set virtualscripts=%1\%virtualfolder%\Scripts\
set virtualactivate=%virtualscripts%activate.bat
set virtualdeactivate=%virtualscripts%deactivate.bat
set getexe=%~dp0GetExecutable.txt

REM The pushd allows the script to deal with UNC paths however
REM if the batch script terminates abnormally then the drive letter
REM that was created by the script will remain.
pushd %1

REM Grab the first line of the script file
REM This will fail if the line endings are not windows
set /p firstline=<%2

REM If the virtual environment exists then activate it
REM echo %virtualactivate%
IF EXIST %virtualactivate% (
	call %virtualactivate%
	echo Virtual
)

REM If the first line is a shebang line which is identified as the first
REM two characters being "#!". Then write that line to a temp file else
REM wipe the temp file out since it is reused every time
IF "%firstline:~0,2%"=="#!" (
	echo %firstline% > %getexe%
) ELSE (
	break > %getexe%
)


REM Write code to the file that will print the path to the Python
REM executable used to stdout
(
	echo import sys
	echo print^(sys.executable^)
) >> %getexe%

REM Run the temp file using the PyLauncher and then save the output to the
REM variable pythonexecutable. Then get the directory in which the Python
REM executable resides.
for /f "delims=" %%i in ('py %getexe%') do set pythonexecutable="%%i"
for %%i in (%pythonexecutable%) do set pythonpath=%%~dpi

REM This is setup for the IPython executable. I am doing it here because of
REM some nonsense about expanding variables that I honestly don't understand
REM but if I do this setup below in the if statements the variables won't get
REM set correctly. Basically what is happening here though is if this is a
REM virtual environment then the python.exe is in the Scripts folder with all
REM the other executables. So we don't need to add Scripts to path to get
REM to the IPython executable.
IF "%pythonpath:~-8%"=="Scripts\" (
	set pythonscriptspath=%pythonpath%
) ELSE (
	set pythonscriptspath=%pythonpath%Scripts\
)

REM Set the path to the IPython executable and the error message if needed
set ipythonexecutable=%pythonscriptspath%ipython.exe
set ipythonerrormsg=IPython executable does not exist at %ipythonexecutable% running Python interactive instead

REM Print the Python version out to the screen
echo Running Python
REM echo %pythonexecutable%
%pythonexecutable% -c "import sys; print(sys.version)"

REM If the third argument is "pdb" then run the script under PDB debugger
REM mode. If the third argument is "ipython" then run the script under
REM a IPython interactive session with PDB mode enabled. Else finally
REM just run the script using the PyLauncher
IF "%3"=="pdb" (
	%pythonexecutable% -m pdb %2
) ELSE IF "%3"=="ipython" (
	IF EXIST "%ipythonexecutable%" (
		"%ipythonexecutable%" -i --pdb %2
	) ELSE (
		echo %ipythonerrormsg%
		%pythonexecutable% -i %2
	)
) ELSE (
	py -W once %2
)

REM Deactivate the virtual environment if it exists and then popd the
REM directory. After which we pause so that any error messages can be viewed.
IF EXIST %virtualdeactivate% call %virtualdeactivate%
popd

pause