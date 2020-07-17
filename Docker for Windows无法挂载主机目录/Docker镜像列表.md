## Docker镜像列表

###  MS SQL Server on Linux

```
docker pull microsoft/mssql-server-linux:latest
docker run -e ACCEPT_EULA=Y -e SA_PASSWORD=<Password here> -p 1433:1433 -d microsoft/mssql-server-linux:latest
```

### 支持VNC的Ubuntu

```
docker pull welkineins/ubuntu-xfce-vnc-desktop
docker run -i -t -p 5900:5900 welkineins/ubuntu-xfce-vnc-desktop
```

### [支持Web-VNC的Ubuntu](https://github.com/fcwu/docker-ubuntu-vnc-desktop)

```
docker pull dorowu/ubuntu-desktop-lxde-vnc
docker run -p 6080:80 -v /dev/shm:/dev/shm dorowu/ubuntu-desktop-lxde-vnc
Browse http://127.0.0.1:6080/
```

### 启用VPN

```
docker run --cap-add=NET_ADMIN -p 6080:80 -v /dev/shm:/dev/shm dorowu/ubuntu-desktop-lxde-vnc

mkdir /dev/net -pv
mknod /dev/net/tun c 10 200
chmod 666 /dev/net/tun

Dockerfile
FROM dorowu/ubuntu-desktop-lxde-vnc

RUN mkdir /dev/net -pv && \
 mknod /dev/net/tun c 10 200 && \
 chmod 600 /dev/net/tun
```

### 从DockerHub删除的[Ubuntu上的Oracle Express Edition 11g](https://github.com/wnameless/docker-oracle-xe-11g)

```
docker pull wnameless/oracle-xe-11g
docker run -d -p 1521:1521 wnameless/oracle-xe-11g

hostname: localhost
port: 1521
sid: xe
username: system
password: oracle
```

### Ubuntu上的Oracle Express Edition 11g

```
docker pull epiclabs/docker-oracle-xe-11g
docker run -d -p 1521:1521 epiclabs/docker-oracle-xe-11g

hostname: localhost
port: 1521
sid: xe
username: system
password: oracle
```

### [Oracle 12c Standard Edition](https://hub.docker.com/r/laboratoriobridge/oracle-12c)

```
docker pull laboratoriobridge/oracle-12c
docker run -d -p 8888:8080 -p 1521:1521 laboratoriobridge/oracle-12c

hostname: localhost
port: 1521
sid: xe
service name: xe
username: system / sys (SYSDBA)
password: oracle
```

### [Fine Report](https://github.com/juglans/finereport)

```
docker pull juglans/finereport
docker run -d -p 8080:8080 juglans/finereport
```

### MariaDB

```
docker pull mariadb
docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=password mariadb
```

### [Node-RED](https://nodered.org/)

```
docker pull nodered/node-red-docker
docker run -it -p 1880:1880 nodered/node-red-docker
```

### [Jupyter Notebook](https://github.com/dirkarnez/docker-jupyter-notebook)

### [Apache PHP](https://github.com/dirkarnez/docker-php-apache)

### Docker技巧

- 设置时区 `RUN echo "Asia/Shanghai" > /etc/timezone;`
- 设置主机文件，必须在一行中 `CMD echo "ip hostname" >> /etc/hosts && ./you-application`
- 设定权利 `RUN chmod -R 777 /root`

### 常见Dockerfile命令

- `RUN` 命令在构建docker映像时触发
- `CMD` 启动创建的docker映像时命令触发

### 常用Docker CLI命令

- `docker system prune -a --volumes` 删除所有内容

### 常见Dockerfile片段

```
RUN apt-get update -y \ 
&& apt-get -y --no-install-recommends install \
   build-essential \
   libgomp1 \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
```



REM 停止并卸下当前容器
docker stop my_deploy_container
docker rm my_deploy_container

REM 仅在需要清除地形本地状态时才删除音量
REM docker volume rm tfstate

REM 建立具有任何更新的图像
docker build -t my_deploy_image -f deploy.docker .

REM 如果命名卷不存在，则创建一个新卷（如果存在，则失败，没关系。）
docker volume create --name tfstate

REM 使用名称和一个env文件运行该映像。
docker run --name my_deploy_container --env-file ./dev.env -v tfstate:/tf/state my_deploy_image



docker run -it ubuntu /bin/bash

REM DEMO:
REM 1. 运行一些UNIX命令以显示与容器的交互
REM 2.查看状态 "docker container ps"
REM 3.所有容器 "docker container ps -a"
REM 4. > docker ps
REM 5. > docker attach bluh
REM 6. > docker stop bluh
REM 7. > docker rm <containerid>