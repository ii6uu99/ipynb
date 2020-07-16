set ABS_PATH=%~dp0

call %ABS_PATH%_cleanup.bat

echo ===================================================
echo  Machine successfully started. Now you can run:
echo  'docker' command from this terminal, i.e.:
echo      docker ps
echo  If you want to use docker from another terminal
echo  you should run start.bat first.
echo ===================================================
