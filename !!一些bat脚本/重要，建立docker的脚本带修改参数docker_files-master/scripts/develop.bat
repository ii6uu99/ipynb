set image=my_image
set name=%image%
set host_port=80
set container_port=80
set env = ''

docker container run --name %name% -e %env% -p host_port:container_port -v %cd%:/home/rails -d %image% \
&& docker container exec -it %name% bash
