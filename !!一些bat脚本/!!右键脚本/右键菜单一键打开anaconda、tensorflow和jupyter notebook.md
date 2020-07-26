右键菜单一键打开anaconda、tensorflow和jupyter notebook

————————————————
通过修改注册表的方法，在右键菜单集成一个按键，一键打开anaconda、tensorflow和jupyter。
代码：

Windows Registry Editor Version 5.00
[HKEY_CLASSES_ROOT\Directory\Background\shell\Anaconda3]
@="Anaconda3 Prompt Here"
"Icon"="你的anaconda路径\\Menu\\Iconleak-Atrous-Console.ico"
[HKEY_CLASSES_ROOT\Directory\Background\shell\Anaconda3\command]
@="cmd.exe /s /k \"title Anaconda3\" && 你的anaconda路径\\Scripts\\activate.bat 你的anaconda路径 && activate tensorflow && jupyter notebook"



使用方法：
复制上面的代码到一个新建的txt文件中，带入你的anaconda路径后保存为reg文件，然后双击运行即可。

在文件夹的空白处右键，效果如下：

进阶：

@="cmd.exe /s /k \"title Anaconda3\" && 你的anaconda路径\\Scripts\\activate.bat 你的anaconda路径 && activate tensorflow && jupyter notebook"



&&是来连接两个命令。当你只想打开tensorflow 的时候，你可以去掉&& activate tensorflow。
————————————————
版权声明：本文为CSDN博主「HaneIP」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/s5821305/article/details/87890864