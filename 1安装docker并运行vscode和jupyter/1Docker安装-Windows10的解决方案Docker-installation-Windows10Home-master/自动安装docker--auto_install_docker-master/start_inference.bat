SET STARTTIME=%TIME%
SET /A STARTTIME=(1%STARTTIME:~0,2%-100)*360000 + (1%STARTTIME:~3,2%-100)*6000 + (1%STARTTIME:~6,2%-100)*100 + (1%STARTTIME:~9,2%-100)
:CHECK_DOCKER_STATUS
FOR /f "tokens=*" %%a IN ('docker ps ^| findstr NAMES') DO (
	docker login 124.9.14.15:443 -u owen -p P@ssw0rd
	docker pull 124.9.14.15:443/inference
	docker run -it -d -p 7500:7500 --name inference 124.9.14.15:443/inference python3 /root/inference_engine/inference.py
	docker start inference
	EXIT
)
TIMEOUT /T 10
SET ENDTIME=%TIME%
SET /A ENDTIME=(1%ENDTIME:~0,2%-100)*360000 + (1%ENDTIME:~3,2%-100)*6000 + (1%ENDTIME:~6,2%-100)*100 + (1%ENDTIME:~9,2%-100)
SET /A DURATION=%ENDTIME%-%STARTTIME%
ECHO DURATION: %DURATION% in centiseconds
IF %DURATION% GEQ 60000 GOTO EXIT
GOTO CHECK_DOCKER_STATUS
PAUSE