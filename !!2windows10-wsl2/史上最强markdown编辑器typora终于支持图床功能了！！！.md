# 史上最强markdown编辑器typora终于支持图床功能了！！！

[![img](https://upload.jianshu.io/users/upload_avatars/22049292/ca57b1ae-61a4-4963-b409-a1c25efb5ffc.jpeg?imageMogr2/auto-orient/strip|imageView2/1/w/96/h/96/format/webp)](https://www.jianshu.com/u/80efab8ba003)

[夏2同学](https://www.jianshu.com/u/80efab8ba003)关注

0.1722020.04.30 00:17:34字数 510阅读 516

## 图床功能教程

markdown编辑器中的王者typora，终于支持自动将图片上传到服务器，返回url了。

![img](https://upload-images.jianshu.io/upload_images/22049292-6c04d4841df5c49f.png?imageMogr2/auto-orient/strip|imageView2/2/w/84/format/webp)

$B`0P}M6W%CKF$93%6J3A6C

终于不用先把图片拖到图床里面再上传了。泪奔。

#### 先来看看效果吧。

![img](https://upload-images.jianshu.io/upload_images/22049292-2be1a888451a4c76.gif?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

giftest

注意上面图片的url变化，从一个本地磁盘上的链接，变成了服务器上的链接。

这也就是说我们再不需要来回折腾。

在typora中编写好markdown文本，直接就可以通过**导入功能**，发到博客里面了。

![img](https://upload-images.jianshu.io/upload_images/22049292-40e6bc1cb9bdc9ba.jpg?imageMogr2/auto-orient/strip|imageView2/2/w/600/format/webp)

分隔乌鸦

那么怎么才能体验到这个功能。

1. 确保typora的版本在0.9.86以上

[图片上传失败...(image-5432f4-1588176970986)]

1. 打开typora，点开最上面的帮助，点击里面的检测更新，先升级一下版本，确保能用。

![img](https://upload-images.jianshu.io/upload_images/22049292-82856d3738dcdc22.png?imageMogr2/auto-orient/strip|imageView2/2/w/596/format/webp)

image-20200429203725223

1. 接着点开 最上面的文件，点倒数第二个**偏好设置**

![img](https://upload-images.jianshu.io/upload_images/22049292-148c4532d5df0f04.png?imageMogr2/auto-orient/strip|imageView2/2/w/479/format/webp)

image-20200429203921405

1. 点击图像

![img](https://upload-images.jianshu.io/upload_images/22049292-4a68f1074aa19e60.png?imageMogr2/auto-orient/strip|imageView2/2/w/905/format/webp)

image-20200429203951593

1. 按照我下面的图，进行选择。

![img](https://upload-images.jianshu.io/upload_images/22049292-dacb0551b6fce831.png?imageMogr2/auto-orient/strip|imageView2/2/w/905/format/webp)

image-20200429204112083

1. 点击下载或更新

![img](https://upload-images.jianshu.io/upload_images/22049292-2d348d5b34ca566a.png?imageMogr2/auto-orient/strip|imageView2/2/w/573/format/webp)

image-20200429204220668

1. 复制下面这条链接，并注册账号

[https://sm.ms/home/apitoken](https://links.jianshu.com/go?to=https%3A%2F%2Fsm.ms%2Fhome%2Fapitoken)



```cpp
![image-20200429204404976](https://upload-images.jianshu.io/upload_images/22049292-69df7a1d1e5d3674.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240) 
```

1. 登录你注册的账号（注意用户名是用户名，不是邮箱），接着复制下面的链接，再次访问

[https://sm.ms/home/apitoken](https://links.jianshu.com/go?to=https%3A%2F%2Fsm.ms%2Fhome%2Fapitoken)

1. 然后，你就进入到这个页面

![img](https://upload-images.jianshu.io/upload_images/22049292-42b6eb168f07d521.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

image-20200429204623154

![img](https://upload-images.jianshu.io/upload_images/22049292-64cd92db045f08b7.png?imageMogr2/auto-orient/strip|imageView2/2/w/827/format/webp)

image-20200429204717704

1. 回到你的typora，点击打开配置文件

![img](https://upload-images.jianshu.io/upload_images/22049292-584bf40f78e18d2f.png?imageMogr2/auto-orient/strip|imageView2/2/w/905/format/webp)

image-20200429204856874

1. 将下面代码复制粘贴到你的配置文件中。

{
"picBed": {
"uploader": "smms", // 代表当前的默认上传图床为 SM.MS,
"smms": {
"token": "这里面的token换成你上个页面的申请的token" //一定要换
}
},
"picgoPlugins": {} // 为插件预留
}

![img](https://upload-images.jianshu.io/upload_images/22049292-6df72c07ad798199.png?imageMogr2/auto-orient/strip|imageView2/2/w/827/format/webp)

image-20200429204717704

1. 保存这个json文件。好了，大工告成！！！

![img](https://upload-images.jianshu.io/upload_images/22049292-0d2cce69dc5e20d0.jpg?imageMogr2/auto-orient/strip|imageView2/2/w/60/format/webp)

害羞

1. 点开验证图片上传。测试一下吧。

![img](https://upload-images.jianshu.io/upload_images/22049292-fafe17261d2ce6f2.png?imageMogr2/auto-orient/strip|imageView2/2/w/905/format/webp)

image-20200429205210300

![img](https://upload-images.jianshu.io/upload_images/22049292-fbf79ccda5b5c76e.png?imageMogr2/auto-orient/strip|imageView2/2/w/905/format/webp)

image-20200429205309996

本文里的图片就是全部用typora自动上传服务搞的。体验很棒。

好了，这就是全部内容，如果觉得对你有帮助，就点个赞吧。

![img](https://upload-images.jianshu.io/upload_images/22049292-9313d6088a018a1c.jpg?imageMogr2/auto-orient/strip|imageView2/2/w/640/format/webp)

求赞

么么哒