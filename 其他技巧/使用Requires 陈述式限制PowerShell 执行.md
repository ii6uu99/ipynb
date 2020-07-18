# 使用Requires 陈述式限制PowerShell 执行

APRIL 7TH, 2020

有些PowerShell指令是需要先安装某些模组，或需要特定权限才能执行，我们如何限制某个PowerShell指令档或模组，在执行前先去检查环境是否符合该指令码的需求，透过`#Requires`陈述式，可以帮我们做到相关限制。

透过使用`#Requires`陈述式，可以现在该PowerShell指令码是否符合指定的PowerShell版本、环境是否安装必要的模组、执行权限是否为系统管理员，如果不符合必要条件，则指令码将无法执行。

`#Requires` 陈述式只能用在Script 指令码中，可以写在指令码中的任何一行，但必须是从该行的第一个陈述式，而一般建议写在档案的开头，方便阅读，同时你也可以写多行来做限制，基本使用方式如下：

```
#Requires -Assembly { <Path to .dll> | <.NET assembly specification> }
#Requires -Version <N>[.<n>]
#Requires -Modules { <Module-Name> | <Hashtable> }
#Requires -PSEdition <PSEdition-Name>
#Requires -PSSnapin <PSSnapin-Name> [-Version <N>[.<n>]]
#Requires -ShellId <ShellId> -PSSnapin <PSSnapin-Name> [-Version <N>[.<n>]]
#Requires -RunAsAdministrator
```

`#Requires` 用到的参数说明：

- `-Assembly` 限制dll 的使用路径或[].NET Assembly 的组件版本名称](https://docs.microsoft.com/zh-tw/dotnet/standard/assembly/names)
- `-Version` 限制PowerShell 最低版本
- `-Modules` 限制PowerShell 执行阶段必须安装所相依的模组
- `-PSEdition`限制PowerShell版本，设定值为`Core`代表PowerShell Core，`Desktop`代表Windows PowerShell
- `-PSSnapin`指定[Snap-in嵌入式管理单元](https://docs.microsoft.com/zh-tw/powershell/scripting/developer/cmdlet/modules-and-snap-ins)
- `-ShellId`指定Shell环境，必须搭配`-PSSnapin`一起设定，可以在PowerShell中执行`$ShellId`来查询当前Shell名称
- `-RunAsAdministrator` 限制执行此指令码必须要有系统管理员权限

> 完整的使用方式及范例请参考[Microsoft PowerShell Docs - About Requires](https://docs.microsoft.com/zh-tw/powershell/module/microsoft.powershell.core/about/about_requires)。

## 常见用法

最常使用到的，应该是以下3 种，留下范例供参考：

```
# 限制執行時必須要有系統管理者權限
#Requires -RunAsAdministrator
# 限制 PowerShell 最低版本為 6.0
#Requires -Version 6.0
# 限制 PowerShell 執行環境必須安裝 AzureRM.Netcore 和 PowerShellGet 模組
#Requires -Modules AzureRM.Netcore, PowerShellGet
# 限制 PowerShell 執行環境必須安裝 AzureRM.Netcore v0.13 以上版本
#Requires -Modules @{ ModuleName="AzureRM.Netcore"; ModuleVersion="0.13.0" }
```

------

参考资料：

- [Microsoft PowerShell Docs - About Requires](https://docs.microsoft.com/zh-tw/powershell/module/microsoft.powershell.core/about/about_requires)
- [PowerShell 技能连载- 探讨Windows PowerShell 和PowerShell Core](https://blog.vichamp.com/2017/07/18/dealing-with-windows-powershell-and-powershell-core/)