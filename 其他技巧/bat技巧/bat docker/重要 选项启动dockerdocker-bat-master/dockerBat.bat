@echo off
cls
:start
echo.
echo 1. Check Container Docker
echo 2. Running Container Nginx
echo 3. Running Container Redis
echo 4. Running Container Mysql
echo 5. Running Nginx,Mysql,redis 
echo 6. Exit
echo.
echo.
set /p pilihan=pilih Task Yang Akan Di Jalankan:
IF '%pilihan%' == '%pilihan%' GOTO Item_%pilihan%
:Item_1
docker ps
goto Start
:Item_2
cd "D:\Dev\Laravel-Projects\laradock"
docker-compose up -d nginx workspace
echo Container Nginx Berhasil Di Running
echo Berikut List Container Yang Aktif
docker ps
goto Start
:Item_3
cd "D:\Dev\Laravel-Projects\laradock"
docker-compose up -d redis workspace
echo Container Redis Berhasil Di Running
echo Berikut List Container Yang Aktif
docker ps
goto Start
:Item_4
cd "D:\Dev\Laravel-Projects\laradock"
docker-compose up -d mysql workspace
echo Container Mysql Berhasil Di Running
echo Berikut List Container Yang Aktif
docker ps
goto Start
:Item_5
cd "D:\Dev\Laravel-Projects\laradock"
docker-compose up -d nginx mysql redis workspace
echo Container Nginx Berhasil Di Running
echo Berikut List Container Yang Aktif
docker ps
goto Start
:Item_6
exit


