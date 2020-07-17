@FOR /f "tokens=*" %%i IN ('docker-machine env Docker') DO @%%i

pause