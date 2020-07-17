for %%I in (.) do set curr=%%~sI
docker run -d -p 8080:80 -p 8443:443 -p 8022:22 ^
-v %curr%\html:/var/www/html ^
-v %curr%\database:/var/lib/phpMyAdmin/upload ^
-t otherdata/centos-docker-lamp:latest ^
--name lamp
