https://github.com/Comsta/packages_vscode

# packages_vscode

vs代码的外部软件包，我用于在角度和打字稿项目中进行编码

## 在源mashine上创建一个批处理文件

继续输入cmd promt并输入:

> for /F "tokens=*" %i in ('code --list-extensions') do @echo call code --install-extension %i >> install.cmd

这将创建一个名为install.cmd的批处理文件

将此批处理文件复制到目标mashine并在cmd控制台中运行

### 在这个仓库中，您可以找到我在Angular项目中实际使用的vs代码插件。