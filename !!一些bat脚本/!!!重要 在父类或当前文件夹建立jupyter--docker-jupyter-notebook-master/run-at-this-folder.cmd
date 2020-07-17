docker pull jupyter/base-notebook:latest
docker run --rm -it -p 8888:8888 -v "%~dp0:/home/jovyan/my-notebooks" jupyter/base-notebook:latest
