# git遇到的问题之“Please make sure you have the correct access rights and the repository exists.”

![img](https://csdnimg.cn/release/phoenix/template/new_img/reprint.png)

[jingtingfengguo](https://me.csdn.net/jingtingfengguo) 2016-07-12 21:46:30 ![img](https://csdnimg.cn/release/phoenix/template/new_img/articleReadEyes.png) 255184 ![img](https://csdnimg.cn/release/phoenix/template/new_img/tobarCollect.png) 收藏 66

分类专栏： [git](https://blog.csdn.net/jingtingfengguo/category_6308896.html)

对于git的提交一直很小心翼翼，感觉一不小心就会踩到莫名的坑。



这不，



某天commit 就遇到了On branch master nothing to commit (working directory clean) 



一查意思。你的分支很干净？



干净？excuse me？



然后git push origin master一下，漫长等待了弹出了fail：#￥%@（此处省略，我们看重点）



Please make sure you have the correct access rights and the repository exists.



然后谷歌了一下，原来是ssh key有问题，连接不上服务器~~

然后我开始了死胡同~~

![img](https://img-blog.csdn.net/20160712215639938)



参阅了很多的答案，发现写的都不是很完整，自己东摸索西摸索搞定了，怕忘记，记录一下



1、首先我得重新在git设置一下身份的名字和邮箱（因为当初都忘了设置啥了，因为遇到坑了）进入到需要提交的文件夹底下（因为直接打开git Bash，在没有路径的情况下，根本没！法！改！刚使用git时遇到的坑。。。）

git config --global user.name "yourname"

git config --global user.email“your@email.com"

注：yourname是你要设置的名字，your@email是你要设置的邮箱。



2、删除.ssh文件夹（直接搜索该文件夹）下的known_hosts(手动删除即可，不需要git）



3、git输入命令

$ ssh-keygen -t rsa -C "your@email.com"（请填你设置的邮箱地址）



接着出现：

Generating public/private rsa key pair.

Enter file in which to save the key (/Users/your_user_directory/.ssh/id_rsa):



请直接按下回车



然后系统会自动在.ssh文件夹下生成两个文件，id_rsa和id_rsa.pub，用记事本打开id_rsa.pub



将全部的内容复制



4、打开https://github.com/，登陆你的账户，进入设置



进入ssh设置

![img](https://img-blog.csdn.net/20160712221858092)

![img](https://img-blog.csdn.net/20160712221921074)



在key中将刚刚复制的粘贴进去

![img](https://img-blog.csdn.net/20160712222026735)

点击add ssh key，



ok！



5、在git中输入命令：



ssh -T git@github.com



然后会跳出一堆话。。



输入命令：yes



回车



然后就会提示你成功了~~



泪牛满面~~



![img](https://img-blog.csdn.net/20160712222732046)

最后退出git重新进入路径提交一下就可以了~~