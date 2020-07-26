# WSL小技巧：切换到zsh以及加入右键菜单

[![img](https://upload.jianshu.io/users/upload_avatars/8869373/142ae248-304f-4418-a045-02f269d419f3.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/96/h/96/format/webp)](https://www.jianshu.com/u/965b95853b9f)

[画星星高手](https://www.jianshu.com/u/965b95853b9f)关注

2018.07.23 21:24:08字数 408阅读 1,225

## 切换到zsh

### 说明

在 Windows Subsystem for Linux 中，执行 chsh -s /bin/zsh 并不能成功地将默认 shell 修改为 zsh。在打开 WSL 时，默认 shell 仍然为 bash。 这是因为WSL 在启动时并没有执行 login 相关的组件，而这些组件和默认 shell 有关。Microsoft 已经知晓了这个问题，但并没有计划去解决。

### 方法

我们可以通过一个简易的 workaround 可以使在打开 WSL 时同时打开 zsh。
在 ~/.bashrc 中添加



```bash
bash -c zsh
```

### 参考资料

https://github.com/Microsoft/WSL/issues/477

## 加入右键菜单

1. 打开运行，输入 `regedit` 运行注册表编辑器
2. 找到注册表中这个文件夹`\HKEY_CLASSES_ROOT\Directory\Background\shell\`
3. 选中shell这个文件夹右键新建一个项，双击默认这个值，改为`WSL Shell Here`，这个是右键菜单显示出来的名字
4. 在默认下面加一个字符串值，名称为`Icon`，双击将它的值改为你想要的图标的地址，可以是`.ico`和`.exe`文件
5. 在 `WSL Shell Here` 下新建一个项，项名称为`command`，将这个项的默认的值改为Ubuntu的exe文件地址，我的是`"C:\Windows\System32\bash.exe"`，注意两边要双引号

![img](https://upload-images.jianshu.io/upload_images/8869373-9d478424db87c804.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

外出中。只能用笔记本上的Windows啦

> Ps: 为什么今天的截图是这样的呢 = =..
> 原因：外出中。只能用笔记本上的Windows啦