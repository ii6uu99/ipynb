# Docker for Windows无法挂载主机目录

Docker for Windows无法挂载主机目录的原因是：主机用于挂载的目录所在盘符没有勾选为`Shared Drives`。

**但是我遇到了这样的情况：**
 之前明明运行的好好的 mysql容器，突然无法挂载主机目录，数据库都不见了。查看容器中挂载点，根本没有被主机目录覆盖，容器启动时貌似也没有报错，直接就给启动了。（之前是可以挂载的，`Shared Drives`也是设置好的）

参考了此文：[win10 docker 使用run -v 时，虚拟机无法显示宿主机挂载的目录 - CSDN博客](https://blog.csdn.net/ap10062kai/article/details/79232582)，他说由于自己更改了windows的密码，需要重新认证。

才想起前段时间，自己将windows的本地账户转换为了在线账户，应该是这个问题。

**解决步骤：**

`Docker Setting > Shared Drives > Reset credentials...`

apply----这时需要密码，即为你windows用户的开机密码。



 然后在弹出的对话框中输入你的在线账户的密码（也就是你电子邮箱的密码）；如果是更改了本地账户密码则输入新的密码。

主机用于挂载的目录位于`G:`盘，所以记得把它勾上。

![img](https:////upload-images.jianshu.io/upload_images/7667789-d233142276646e33.png?imageMogr2/auto-orient/strip|imageView2/2/w/832/format/webp)

Docker Reset credentials.png



作者：faner
链接：https://www.jianshu.com/p/47def5fef04b
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。





方法一
　　
　　winpty docker run -itv "/C:www.michenggw.com /Users/cb/DockerPackages":/mnt/packages centos:7
　　
　　方法二
　　
　　winpty docker run -i -t -v "/C:www.yigouyule2.cn \users\bin.chen\DockerPackages":/mnt/packages centos:7
　　
　　方法三
　　
　　winpty docker run -i -t -v "C:\users\bin.www.mingcheng178.com chen\DockerPackages":/mnt/packages centos:7
　　
　　由此看来，开头是不是用/不是很重要。而""是必须的。暂时没有找到可以使用~的方案，如果有，请留言告诉我。
　　
　　其次，在windows下使用路径，在写:/的时候要非常慎重，这个会被补全或者转义，务必在最前面加上/。







docker: Error response from daemon: D: drive is not shared. Please share it in Docker for Windows Settings.

Docker在发布网页时，需要把容器的文件夹和本地进行挂载，把网页放在共享的文件夹内。

docker run -t -i -v /d/PycharmProjects:/test nginx --name mynginx2 /bin/bash

需要用到-v的参数来指定相互绑定的文件夹的名字，写法很特殊D盘为/d等。

同时你需要在Docker of windows的Setting 中进行配置，将盘符进行共享。这时需要密码，即为你windows用户的开机密码。
————————————————
版权声明：本文为CSDN博主「裴小强」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_35723062/article/details/80989662





















