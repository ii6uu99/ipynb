@echo off

>images.txt (
	docker images -f "dangling=true" -q 
)

for /f "delims=" %%i in (images.txt) DO ( 
  docker rmi %%i
)

del images.txt

echo "Dangling Images removed"