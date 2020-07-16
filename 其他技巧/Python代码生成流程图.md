# Python 一键转化代码为流程图

[![松鼠爱吃饼干](https://pic2.zhimg.com/v2-23f8a62028768fe51eb03c543b685a08_xs.jpg?source=172ae18b)](https://www.zhihu.com/people/wan-wan-33-7)

[松鼠爱吃饼干](https://www.zhihu.com/people/wan-wan-33-7)

python学习交流

2 人赞同了该文章





![img](https://picb.zhimg.com/80/v2-ee5160cc084d527280f487c10a138a85_720w.jpg)


Graphviz是一个可以对图进行自动布局的绘图工具，由贝尔实验室开源。我们在上次 Python 快速绘制画出漂亮的系统架构图 提到的diagrams，其内部的编排逻辑就用到了这个开源工具包。
而今天我们要介绍的项目，就是基于Python和Graphviz开发的，能将源代码转化为流程图的工具：pycallgraph。


**1.准备**
开始之前，你要确保Python和pip已经成功安装在电脑上噢，如果没有，请访问这篇文章：超详细Python安装指南 进行安装。如果你用Python的目的是数据分析，可以直接安装Anaconda：Python数据分析与挖掘好帮手—Anaconda
Windows环境下打开Cmd(开始—运行—CMD)，苹果系统环境下请打开Terminal(command+空格输入Terminal)，准备开始输入命令安装依赖。
当然，我更推荐大家用VSCode编辑器，把本文代码Copy下来，在编辑器下方的终端运行命令安装依赖模块，多舒服的一件事啊：Python 编程的最好搭档—VSCode 详细指南。
在终端输入以下命令安装我们所需要的依赖模块:

```text
pip install pycallgraph
```

看到 Successfully installed xxx 则说明安装成功。
macOS用户请使用brew安装：

```text
brew install graphviz
```

windows用户请点击链接下载安装：

```text
https://pythondict.com/go/?url=https://graphviz.gitlab.io/_pages/Download/windows/graphviz-2.38.msi
```

安装完成后需要将其写入到环境变量中：

![img](https://pic3.zhimg.com/80/v2-e527d9b5e4b2c9ea92b37ff9cf81047a_720w.jpg)


**2.生成流程图**
该模块有两种调用方式，一种是在代码里通过上下文调用：

![img](https://picb.zhimg.com/80/v2-8fd245217add50ae2f945eaf5814cb61_720w.jpg)


比如说，绘制一下咱上回的《Python 我的世界》源代码的流程图：

![img](https://pic4.zhimg.com/80/v2-47c5fdb0d5f93ef4593374b5dd673422_720w.jpg)



在运行该Python文件后，会在当前文件夹下产生一个pycallgraph.png的文件，这个就是该代码的流程图：



![img](https://pic2.zhimg.com/80/v2-dea33ced05cd387c5b3a0a2f02fa2be9_720w.jpg)



还有一种是使用命令的方式调用，这个方式必须使用bash才能运行，macOS用户可以忽视这个问题，但如果你是windows用户，请通过以下方式打开bash（以VS Code为例）：



![img](https://pic4.zhimg.com/80/v2-7220c827f80a402708826eadcb827ec8_720w.jpg)



![img](https://pic3.zhimg.com/80/v2-67b535adb1ad4fd17c164a9e08338457_720w.jpg)



输入以下命令生成流程图：

```text
pycallgraph graphviz -- ./你需要生成流程图的.py文件
```

完成后会在当前文件夹下生成一个pycallgraph.png的文件，这个就是这份代码的流程图。

![img](https://pic1.zhimg.com/80/v2-f41afaaf9a100309202143c2a9f77ebb_720w.jpg)


通过这个方法，你可以清晰地看到这份源代码里面的调用逻辑和其每个模块的运行时间，是一个很方便的小工具，非常适合初学者学习他人的开源模块。大家有需要研究的代码可以用这个工具试一试，说不定有意外的收获呢。