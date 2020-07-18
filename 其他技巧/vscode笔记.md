# Visual Studio 笔记

JANUARY 1ST, 1970

本篇作为书签用途，记录网路上的Visual Studio 相关资讯

## 维持Visual Studio 2019 跑得又快又好的技巧

1. 载入方案时不要重新开启文件
   - 预设可能会开启大量文件，会拖慢整体载入速度。
   - 工具> 选项> 专案和方案> 一般> 在解决方案载入时重新开启文件
2. 载入方案时不要还原专案阶层状态
   - 这会记忆大量状态，且每个都需要还原，因次可以设定预设不还原专案阶层状态。
   - 工具> 选项> 专案和方案> 一般> 还原解决方案载入上的方案总管专案阶层状态 ![载入方案时不要重新开启文件及还原专案阶层状态](https://i.imgur.com/ZpFQU3w.png)
3. 预设关闭所有不需要的工具窗格
   - 因为有许多窗格预设就会开启(Team Explorer, Error, Output, …)且无法设定预设关闭，所以可安装[Reset Tool Windows](https://marketplace.visualstudio.com/items?itemName=MadsKristensen.ResetToolWindow)扩充套件，它会在VS开启时自动关闭这些一定会被开启的工具窗格，节省载入时间。
   - 工具> 选项> 环境> 启动> Reset Tool Window ![预设隐藏所有不需要的工具窗格](https://i.imgur.com/nFt25tj.png)

## 快捷键

| 快速键             | 说明                                       |
| :----------------- | :----------------------------------------- |
| Ctrl+ ],S          | 可快速跳到Solution Explorer 该档的所在位置 |
| Alt + 上下的方向鍵 | 快速将程式码上、下搬动                     |
| Ctrl+ K,D          | 格式化文件                                 |
| Ctrl + Space       | IntelliSense 程式码自动完成                |
| Ctrl+ K,C          | 注解程式码                                 |
| Ctrl+ K,U          | 取消注解程式码                             |
| Ctrl+ R,R          | 重新命名                                   |
| F12                | 移至定义                                   |
| Ctrl + F12         | 移至实作                                   |
| Ctrl + -           | 搭配`F12` 移至定义，此为返回至原位置       |
| F8                 | 移至下一个错误位置                         |
| Shift + Delete     | 删除整行                                   |
| Ctrl+ Shift+ Click | 选取多个游标位置                           |

## 必装套件

- Whack Whack Terminal

  - 终端机模拟器，让你可以在Visual Studio 中开启各种终端机，如command prompt、powershell、WSL bash
  - 快速键`Ctrl`+ `\`, `Ctrl`+`\`

- BuiltinCmd

  - 终端机模拟器
  - 快速键`Ctrl`+ `Shift`+`T`

- CodeMaid

  - 自动程式排版，快速键`Ctrl`+ `M`, `空白鍵` _检视各个Method的循环复杂度

- Visual Studio Spell Checker

  - 检查程式码英文拼写是否正确
  - [介绍文](https://blog.poychang.net/visual-studio-spell-checker/)

- Web Essentials

  - Web Essentials 是增强Visual Studio 在Web、CSS、JavaScript 开发上的方便性
  - 再加装[Web Extension Pack](https://visualstudiogallery.msdn.microsoft.com/f3b504c6-0095-42f1-a989-51d5fc2a8459?SRC=Home)里面包含很多好用的工具
  - Browser Sync for Visual Studio可以使用`CTRL`+ `Alt`+ `Enter`来启动

- [C# Essentials](https://visualstudiogallery.msdn.microsoft.com/a4445ad0-f97c-41f9-a148-eae225dcc8a5)

- [SideWaffle Templates for Visual Studio 2015](http://sidewaffle.com/)

- Productivity Power Tools

  - 可以取代已经不维护的VSCommands for Visual Studio

- Developer Assistant

  - 写程式时，IntelliSense 列出Method 外，还会列出Sample Code

- tangible T4 Editor 2.3.0 plus modeling tools

  - 程式码产生器编辑器

- Force UTF8

  - 存档时自动转UTF8 with BOM

- [VSCommands for Visual Studio](http://vscommands.squaredinfinity.com/)

  (已停止维护)

  - 利用VSCommands 可以让Visual Studio 变的更聪明些，因为此套件功能相当的多，笔者无法一一介绍，所以就这在里介绍一些较为亮眼的功能。

- Snippet Designer

  - 用更人性化的方式管理我们常用的或内建的Code Snippet 程式码片段

- Glyphfriend

  - 让Intellisense 显示方便辨识的图示

- JavaScript Snippet Pack

  - JavaScript 的Code Snippet

- [Macros for Visual Studio](https://marketplace.visualstudio.com/items?itemName=VisualStudioPlatformTeam.MacrosforVisualStudio) _ [DEMO大的介绍文](http://demo.tc/post/833#.WGomoFFb9cM.facebook) _由于巨集脚本没有同步功能，建议参考「DEMO大的介绍文」设定透过OneDrive同步

- [Snippet Designer](https://marketplace.visualstudio.com/items?itemName=vs-publisher-2795.SnippetDesigner) _自己写一个Code Snippets Template来产生自己要的程式码区段_ [介绍文- Code Snippets产生常用程式码Template](http://limitedcode.blogspot.tw/2015/10/visual-studio-code-snippetstemplate.html)

- Output Enhancer

  - 帮你的输出内容加上颜色，方便阅读

## 图示描述

[类别检视和物件浏览器图示](https://msdn.microsoft.com/zh-tw/library/y47ychfe.aspx)

Visual Studio 2017完整的Icon图示请[下载此连结的PDF档案](https://docs.microsoft.com/en-us/visualstudio/designers/the-visual-studio-image-library?WT.mc_id=DT-MVP-5003022)

[类别检视] 和[物件浏览器] 会显示代表程式码实体(Entity) 的图示，例如：命名空间(Namespace)、类别(Class)、函式和变数。下表说明这些图示：

![Visual Studio 图示描述](http://i.imgur.com/GkxBvNG.jpg)

在方案总管中识别版本控制项目状态：

![Visual Studio 版控项目状态的图示描述](https://i.imgur.com/Ghc8EmI.png)

## 轻量型载入

[官方文件](https://docs.microsoft.com/zh-tw/visualstudio/ide/optimize-visual-studio-startup-time?WT.mc_id=DT-MVP-5003022)提到Visual Studio 2017 15.5版和更新版本不再提供这项功能。

Visual Studio 2017的方案属性页中，有个`輕量型載入`的选项，可以让你在开启方案时，不用一次把底下所有的专案都开启

![轻量型载入](http://i.imgur.com/kpWaP6S.png)

等到你真的要开启该专案的时候，才会真的去载入专案，借此可以加快开启方案的速度

![开启专案时](http://i.imgur.com/W6LATdB.png)

## 关闭npm 套件自动还原

当使用Visual Studio 开启前端专案的时候，Visual Studio 会很贴心的自动帮你把bower 和npm 套件自动还原，不过这些套件通常都很多，下载安装会需要一段时间，如果你想要关闭这个行为了话，可以参考下面步骤：

1. 工具列上的[工具] > [选项]
2. [专案和方案] > [Web Package Management] > [套件还原]
3. 将[在专案开启时还原]改成`false`(参考下图)

![套件还原](https://i.imgur.com/xRgrLqI.png)

## NuGet

Source: https://api.nuget.org/v3/index.json API: https://www.nuget.org/api/v2/

### NuGet 设定Proxy

REF: [NuGet Behind Proxy](https://stackoverflow.com/questions/9232160/nuget-behind-proxy)

使用NuGet.exe 来设定，指令如下：

```
nuget.exe config -set http_proxy=http://my.proxy.address:port
nuget.exe config -set http_proxy.user=mydomain\myUserName
nuget.exe config -set http_proxy.password=mySuperSecretPassword
```

> 如果需要设定帐号、密码，需要用指令来加入，因为此方式会将密码加密。

所执行的相关设定会储存至`C:\Users\{username}\AppData\Roaming\NuGet\NuGet.Config`档案中，当然你也可以直接修改该设定档，只要加入以下设定：

```
<configuration>
    <config>
        <add key="http_proxy" value="http://my.proxy.address:port" />
    </config>
</configuration>
```

上述的路径会是全域的，如果只想针对某个专案或方案来设定，可以再该资料夹下加入`NuGet.Config`档案即可。

> 设定完成后，要重新开启Visual Studio 使其设定生效。

------

参考资料：

- [维持Visual Studio 2019 跑得又快又好的技巧](https://blog.poychang.net/note-visual-studio/#維持-visual-studio-2019-跑得又快又好的技巧)
- [快捷键](https://blog.poychang.net/note-visual-studio/#快捷鍵)
- [必装套件](https://blog.poychang.net/note-visual-studio/#必裝套件)
- [图示描述](https://blog.poychang.net/note-visual-studio/#圖示描述)
- [轻量型载入](https://blog.poychang.net/note-visual-studio/#輕量型載入)
- [关闭npm 套件自动还原](https://blog.poychang.net/note-visual-studio/#關閉-npm-套件自動還原)
- NuGet
  - [NuGet 设定Proxy](https://blog.poychang.net/note-visual-studio/#nuget-設定-proxy)