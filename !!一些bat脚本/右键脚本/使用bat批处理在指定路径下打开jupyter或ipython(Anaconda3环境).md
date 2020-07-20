使用bat批处理在指定路径下打开jupyter或ipython(Anaconda3环境)

注意：这里主要是针对jupyter或ipython需要指定生效路径的操作较为繁琐，经常使用则可以采取这个方法

新建一个txt文件
写入以下批处理脚本
%windir%\System32\cmd.exe  /k "
cd .\ 
& C:\ProgramData\Anaconda3\Scripts\activate.bat C:\ProgramData\Anaconda3 
& *** 
& exit"

这句话主要是执行路径切换、激活Anaconda环境路径、执行所需命令以及退出；
这里的C:\ProgramData\Anaconda3是Anaconda3的默认安装位置，同时将.\修改为所指定的位置，最后将上个命令中的***替换为jupyter notebook或者ipython。

为批处理脚本创建快捷方式，之后便可快捷打开相应的应用了。



miniconda的设置  



%windir%\System32\cmd.exe  /k "
cd .\ 
& C:\ProgramData\miniconda3\Scripts\activate.bat C:\ProgramData\miniconda3\
& *** 
& exit"









————————————————
版权声明：本文为CSDN博主「FlameAlpha」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/Flame_alone/article/details/104271188