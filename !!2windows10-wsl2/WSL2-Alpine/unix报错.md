# [docker安装出现"Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?"](https://www.cnblogs.com/mydailycoding/p/12375352.html)

今天按照这个[教程](https://www.runoob.com/docker/ubuntu-docker-install.html)使用WSL安装docker时遇到了个问题:

- 使用命令:`$ docker search mysql`
- 出现:`Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?`

进一步测试发现其他命令也都不能使用

必应搜索一番之后找到了一些解决方案:例如[这个博客](https://www.cnblogs.com/mmzs/p/12090197.html)

```shell
$ systemctl daemon-reload
$ sudo service docker restart
$ sudo service docker status
```

不过我在执行第一个命令时就出现了:

```
System has not been booted with systemd as init system (PID 1). Can't operate
```

后来找到了这个[issue](https://github.com/MicrosoftDocs/WSL/issues/457)

@**[craigloewen-msft](https://github.com/craigloewen-msft)**

> "Instead of using `sudo systemctl start docker` use: `sudo /etc/init.d/docker start` , as of right now we do not have systemd in WSL 2."

尝试了`sudo /etc/init.d/docker start`启动docker之后便不再出现片头那个问题

参考资料

> https://github.com/MicrosoftDocs/WSL/issues/457
>
> https://www.runoob.com/docker/ubuntu-docker-install.html
>
> https://www.cnblogs.com/mmzs/p/12090197.html