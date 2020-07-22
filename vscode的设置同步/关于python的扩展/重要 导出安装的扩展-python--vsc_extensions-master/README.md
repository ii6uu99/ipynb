# Visual Studio代码扩展

## 导出已安装的扩展

进行安装的扩展名导出到文件，请执行以下操作：

```bash
code --list-extensions | xargs -L 1 echo code --install-extension > <target_file>
```

## 从文件引入扩展名

要从扩展文件导入和安装扩展，请在计算机上执行以下操作：

```bash
source <file_with_extensions>
```

