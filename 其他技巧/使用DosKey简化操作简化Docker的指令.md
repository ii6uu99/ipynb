# 使用DosKey简化操作简化Docker的指令

2018年8月24日

其实只是不仅仅可以用在Docker，或者适用于于各种*长指令*的情境，这里的情境是使用Docker对异步伺服器上的Docker做指令操作时，会透或`-H`的参数指定远端伺服器，而这个参数值会使指令变得很常，不好打之外又不好看，透过DosKey来简化操作指令。

例如要执行像这样的指令：

```
docker -H=docker.server.com logs --tail 100 WebApp
```

这指令是要显示远端`docker.server.com`伺服器的Docker里面的WebApp容器最后100行的log，原本简单的指令因为要加上`-H`变得要打很多字，而且变得很长，此时我们可以写一个cmd指令档如下：

```
;= @echo off
;= rem Call DOSKEY and use this file as the macrofile
;= %SystemRoot%\system32\doskey /listsize=1000 /macrofile=%0%
;= rem In batch mode, jump to the end of the file
;= goto:eof
;= Add aliases below here
remote-docker=docker -H=docker.server.com $*
```

假设这个指令档叫做`docker-alias.cmd`，在终端机中执行完此指令档后，我们的指令就可以改成如下：

```
remote-docker logs --tail 100 WebApp
```

是不是变得易读又简单了。

## DosKey指令介绍

透过呼叫DosKey来编辑终端机命令列，或者建立巨集。

指令详解：

```
DOSKEY [/REINSTALL] [/LISTSIZE=size] [/MACROS[:ALL | :exename]]
       [/HISTORY] [/INSERT | /OVERSTRIKE] [/EXENAME=exename] [/MACROFILE=filename]
       [macroname=[text]]
```

| 参数                  | 说明                                 |
| :-------------------- | :----------------------------------- |
| `/REINSTALL`          | 安装另一份                           |
| `/LISTSIZE=size`      | 设定命令历程司法的大小               |
| `/MACROS`             | 显示所有的Doskey巨集                 |
| `/MACROS:ALL`         | 显示所有执行档中含有Doskey巨集的     |
| `/MACROS:exename`     | 显示指定的执行档中的所有Doskey巨集   |
| `/HISTORY`            | 显示存在记忆体中的所有命令           |
| `/INSERT`             | 指定您所键入的新文字插入在旧的文字中 |
| `/OVERSTRIKE`         | 指定您所键入的新文字覆盖旧的文字     |
| `/EXENAME=exename`    | 指定执行档                           |
| `/MACROFILE=filename` | 指定要安装的巨集档案                 |
| `macroname`           | 为您建立的巨集指定名称               |
| `text`                | 指定您要记录的命令                   |

启动DosKey.exe后，可以使用以下操作：

- 向上与向下键叫回以前的指令
- `ESC` 清除命令列
- `F7` 显示命令历程
- `ALT`+ `F7`清除命令列历程
- `F8` 寻找命令历程
- `F9` 以号码选择命令
- `ALT`+ `F10`清除巨集定义

以下是在Doskey巨集定义中的特殊码：

- `$T` 命令分隔字元。允许在一个巨集中使用多个命令。
- `$1`- `$9`增量档参数。相当于预期档中的`%1`到`%9`。
- `$*` 这个符号代表在命令列中巨集名称后的所有文字。

------

参考资料：

- [BAT指令：DOSKEY的功能介绍](http://forum.twbts.com/thread-10210-1-1.html)
- [如何在Windows命令行中设置别名？](https://superuser.com/questions/560519/how-to-set-an-alias-in-windows-command-line)
- [Microsoft Docs-Windows命令](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/doskey?WT.mc_id=DT-MVP-5003022)