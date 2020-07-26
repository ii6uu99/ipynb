# windows10系统中，WSL文件位置

资源管理器中输入：`\\wsl$`

![img](https://upload-images.jianshu.io/upload_images/18714459-5d3bb2ab0de00c0a.png?imageMogr2/auto-orient/strip|imageView2/2/w/884/format/webp)

对应的路径是
C:\Users\`Melville`\AppData\Local\Packages\`CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc`\LocalState\rootfs
（**根据自己的用户名和WSL系统，替换路径中高亮的部分**）



映射网络驱动器

wsl -l

我的电脑--映射网络驱动器--    \\\wsl$\Ubuntu 





批处理bat映射网络驱动器

net use l: \\wsl$\Ubuntu 









