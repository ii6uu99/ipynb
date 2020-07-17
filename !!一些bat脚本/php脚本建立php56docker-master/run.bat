docker run -d -i  ^
	   --name php56docker ^
	   -p 8000:80 ^
	   -v /c/Users/veni/Desktop/docker/php56docker/www:/var/www/html ^
	   -v /c/Users/veni/Desktop/docker/php56docker/logs:/var/log/httpd ^
veni:php56docker