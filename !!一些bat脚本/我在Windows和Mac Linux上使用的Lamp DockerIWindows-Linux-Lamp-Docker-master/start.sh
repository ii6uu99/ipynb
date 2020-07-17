docker run -d --name lamp -p 8080:80 -p 8443:443 -p 8022:22 \
-v "$PWD"/html:/var/www/html \
-v "$PWD"/database:/var/lib/phpMyAdmin/upload  \
-t otherdata/centos-docker-lamp:latest
