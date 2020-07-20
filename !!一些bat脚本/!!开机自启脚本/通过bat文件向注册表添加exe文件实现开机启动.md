通过bat文件向注册表添加exe文件实现开机启动

1 新建txt 文件 添加如下内容：

@echo off
start  "22" "C:\Windows\System32\cmd.exe" 
reg add HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v SunRAC /t reg_sz /d "%~dp0SunRAC.exe" 
taskkill /f /im cmd.exe
exit

2 修改txt文件后缀名为bat  

3 将bat文件放入需要开机启动的对应exe文件同一个目录

文本内容备注：

第二行： start，负责启动cmd.exe程序。至于22是cmd命令长的名字，可以不写。后面是cmd的存放路径

第三行：是要在cmd中执行的命令 ，其中前一个SunRAC是注册名称，后一个是对应exe文件

第四行是执行完命令后关闭cmd命令窗口

第五行是退出命令

补充说明：貌似一个bin里面最好只有一个bat文件

      注册表查看目录：HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run

   

————————————————
用批处理文件在注册表中添加开机启动项

reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v myauto /t REG_SZ /d C:\1.bat /f

/v 新增的键名    

/t REG_SZ   新增的键值类型

/d 新增的键值

/f  强制改写现有表项不提示



————————————————



1.Run键

　　Run键是病毒最青睐的自启动之所，该键位置是[HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run]和[HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run]，其下的所有程序在每次启动登录时都会按顺序自动执行。

　　还有一个不被注意的Run键，位于注册表[HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run]和[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run]，也要仔细查看。

　　2.RunOnce键

　　RunOnce位于[HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunOnce]和[HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnce]键，与Run不同的是，RunOnce下的程序仅会被自动执行一次。

　　3.RunServicesOnce键

　　RunServicesOnce键位于[HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunServicesOnce]和[HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunServicesOnce]下，其中的程序会在系统加载时自动启动执行一次