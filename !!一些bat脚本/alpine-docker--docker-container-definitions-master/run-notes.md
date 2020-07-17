# Running docker images

## Example

```
docker run --name=nginx -d -v ~/nginxlogs:/var/log/nginx -p 5000:80 nginx
```

--name=nginx                    names the container so we can refer to it more easily.
-d                              detaches the process and runs it in the background. 
                                Otherwise, we would just be watching an empty Nginx prompt and wouldn't be able to use this terminal until we killed Nginx.

-v ~/nginxlogs:/var/log/nginx   sets up a bindmount volume that links the /var/log/nginx directory from inside the Nginx container 
                                to the ~/nginxlogs directory on the host machine. 
                                Docker uses a : to split the host's path from the container path, and the host path always comes first.

-p 5000:80                      sets up a port forward. 
                                The Nginx container is listening on port 80 by default. 
                                This flag maps the container's port 80 to port 5000 on the host system.




## Connect to a detached container

```
sudo docker attach <container_id>
sudo docker attach <container_name>
```

## Running Travis CI

# choose the image according to the language chosen in .travis.yml
docker run -it -u travis travisci/ci-garnet:packer-1515445631-7dfb2e1 /bin/bash

docker run --name=garnet -v /home/zhixian/data:/var/data -p 55000:80 -it -u travis travisci/ci-garnet:packer-1515445631-7dfb2e1 /bin/bash

# now that you are in the docker image, switch to the travis user
sudo — travis




