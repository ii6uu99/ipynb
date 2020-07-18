# 设置PowerShell的别名

2016年8月5日

当然可以自订，方法也很简单，使用`Set-Alias`指令就可以办到，只是这个别名的生命周期只有这一次的Session有效，那要怎么让它成为永久的别名呢？。

假设我们今天要建立一个别名，，被`ll`取代`Get-ChildItem`（为什么会取`ll`？因为我习惯使用bash的`ls -l`指令…）。

首先，通过以下指令找到PowerShell的设定档`Microsoft.PowerShell_profile.ps1`储存位置

```
Get-Variable profile | Format-List
```

![查找PS1文件位置](http://i.imgur.com/SufCXTz.png)

接者用文字编辑器开启该档案，加入以下程式码

```
Set-Alias ll Get-ChildItem
```

这样我就可以不改变习惯的使用`ll`来显示资料夹内容了〜ohyeah