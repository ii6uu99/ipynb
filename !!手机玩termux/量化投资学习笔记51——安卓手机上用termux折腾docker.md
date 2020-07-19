# 量化投资学习笔记51——安卓手机上用termux折腾docker

[![春城牙医赵瑜敏](https://pic3.zhimg.com/3fd503f27f39fa1e8a9f633ead799393_xs.jpg?source=172ae18b)](https://www.zhihu.com/people/zhao-you-min)

[春城牙医赵瑜敏](https://www.zhihu.com/people/zhao-you-min)

牙医/编程爱好者/骑行爱好者 私信不看病，已开通值乎，欢迎付费咨询。

4 人赞同了该文章

最近两天折腾了一下docker容器，主要的原因是我的亚马逊云服务器快到期了。之前因为我主要在手机上用pydroid3和termux进行python编程，学习机器学习，量化投资等。但有的库在手机上要么装不了，要么装上却用不了。于是弄了个可以免费使用的亚马逊云的E2服务器，在服务器上搭建开发环境。在手机上写程序，再通过scp或者github传到服务器上，在服务器上运行，再把结果传回手机。我的量化投资学习笔记里的代码都是这么完成的。

这么做有点麻烦，我想的是在手机上写好以后，一个命令就可以调用服务器上的开发环境执行程序，结果(比如图片)等就直接保存在本地了。在知乎上提问了，有知友建议用docker容器，我搜了一下，的确能实现我的想法，但是几乎都是用IDE来实现的，有用pycharm的，也有用VS code的，问题是我用的是安卓手机……而且看着还是蛮复杂的，于是就放下了，还是用scp吧。

最近因为免费服务器快到期了，到期我不想续期了，毕竟付的是美元。到期面临着重新在新的服务器上建开发环境的问题。而docker容器正好就是解决这个痛点的神器。于是我决定尝试一下。docker容器是用go语言开发的，它就像一个集装箱。集装箱内部装的东西是各种各样的，但装到集装箱里就以统一的面目示人了。docker就是把程序和程序的运行环境都打包成一个容器(container)，以容器为单位发布，运行。与虚拟机相比，容器要轻量得多，开销要小得多。因此一台设备上可以运行很多的容器。还有一个重要的概念是镜像(image)，是建立容器的模板。可以自己编辑Dockerfile来建立镜像，也可以用别人建立好的镜像，并在此基础上修改，增加新的内容，再把这个新的容器保存为镜像。在docker hub网站上有各种各样建立好的docker镜像。

我先在服务器上折腾，安装了docker，在docker hub网站上注册了账号，用docker pull下载了一个anaconda3的镜像，生成容器以后，在容器里安装了tensorflow，pytorch等库，安装了vim，再根据该容器生成镜像，最后上传到docker hub上。这样换服务器时就不必重新建立开发环境了，下载镜像，生成容器就行了。我的镜像名是zwdnet/mypython。具体过程不再赘述了，参考了两本书:《第一本docker书》和《docker技术入门与实战》。

接下来，我想能不能在termux里也装docker，这样连服务器也可以省了。在网上一搜，还真有在termux里装docker的。不是直接装，而是用虚拟机qemu安装linux虚拟机环境，然后在虚拟机里装docker。

具体过程参考这里:

[Android运行Docker！(Termux + QEMU + linux_alpine, qemu网络映射)stageguard.top![图标](https://pic3.zhimg.com/v2-3c67f19494a3a31d609ae0cd476ca532_180x120.jpg)](https://link.zhihu.com/?target=https%3A//stageguard.top/2019/08/15/run-docker-on-qemu-alpine/%231-Docker)

作者说没啥用，就是折腾。我这不就找到个用处啦？哈哈。就是照文章的过程进行的，注意在我这里用VNC Viewer有问题，主要是用vi编辑，要退出的时候显示"q"未实现，在termux终端里就正常了。另外镜像文件大小最好指定在10G以上。

按照文章安装好docker环境，要准备下载我上传的镜像了。在下载前先按照这篇文章



[Docker镜像源修改_运维_superwind-CSDN博客blog.csdn.net![图标](https://picb.zhimg.com/v2-c86bc0072359fc21529f0d3e90e9620c_ipico.jpg)](https://link.zhihu.com/?target=https%3A//blog.csdn.net/jixuju/article/details/80158493)

更换国内的源，我用的中科大的。

下载过程蛮长的，之后就加载镜像为容器，用tensorflow测试了一下，成功了!注意tensorflow是用conda建了tensorflow环境的，所以要先激活该环境。

![img](https://pic3.zhimg.com/80/v2-39b9c693f7d3079e7640aea128b04cd3_720w.jpg)



有个问题，输出好像不会换行，超出一行的内容就显示不了了。还会出现很多显示混乱的问题。

我在知乎提问了:

[在手机里用qemu装Alpine Linux虚拟机，终端显示不会换行，要如何设置?www.zhihu.com![图标](https://pic3.zhimg.com/v2-aec3fc9255ae74f11214d6382c25a0d9_120x160.jpg)](https://www.zhihu.com/question/394797747)

接下来要解决文件共享的问题，还要探索一下能不能实现不进虚拟机环境而通过ssh等直接调用。

可以在启动虚拟机的命令后面加&，就在后台执行了，然后用

```console
ssh root@localhost -p 2222
```

就可以登陆虚拟机里的linux。

用

```text
scp -P 2222 ../pytorchtest.py root@localhost:~/code
```

可以把文件从宿主机复制到虚拟机里，注意P是大写的。在虚拟机里，用-v选项启动容器，可以在虚拟机和容器之间共享目录。就跟在服务器上一样了。

现在的问题就是能不能直接在termux里调用虚拟机里的开发环境，而不用这一系列的复制文件，登陆等操作。再研究一下吧。





我发文章的三个地方，欢迎大家在朋友圈等地方分享，欢迎点“在看”。

我的个人博客地址：[https://zwdnet.github.io](https://link.zhihu.com/?target=https%3A//zwdnet.github.io/)