# che-install
https://github.com/benoitf/che-install





# 安装

一个用于安装Eclipse Che的Docker安装程序假定已经安装了Docker。

本示例会将./files-to-deliver中的文件移动到./bin/*。如果用户在另一个目录中运行此docker命令，则执行文件将交付到该目录的/ bin文件夹中。此特定示例在交付后运行bin \ test.bat，但是可以对其进行修改。

### 视窗：

```
git clone http://github.com/tylerjewell/che-install
docker build -t local .
launch
```

### Linux / Mac：

```
git clone http://github.com/tylerjewell/che-install
docker build -t local .
docker run -v $(pwd):/che local
```