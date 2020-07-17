docker pull jupyter/base-notebook:latest
for %%A in ("%~dp0..\") do set parent=%%~fA
docker run --rm -it -p 8888:8888 -v "%parent%:/home/jovyan/my-notebooks" jupyter/base-notebook:latest
