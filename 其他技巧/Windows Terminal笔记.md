# Windows Terminal笔记

1970年1月1日

本篇作为书签用途，记录网路上的Windows Terminal相关资讯

## Windows Terminal快速键

- alt+ shift+ +增加左右分割画面
- alt+ shift+ -增加上下分割画面
- alt+ ←或→移动焦点至另一个分割画面

## WSL设定

- [保哥的Windows Linux子系统（WSL）终极开发人员配置-2018版](https://blog.miniasp.com/post/2018/06/15/My-Windows-Subsystem-for-Linux-WSL-Setup-2018)
- [以WSL + Ubuntu + zsh打造Windows上高富帅的命令列模式](https://blog.kkbruce.net/2019/03/wsl-ubuntu-zsh-windows-command-line.html)
- [Windows Linux子系统（WSL）环境设置](https://hackmd.io/@tf-z1zFMTIC8ADhxEcGJEA/BJByCIUHf)

```
# 讓執行 sudo 的時候免輸入密碼
# 請記得將 poy 換成你自己的 WSL 登入帳號
echo "poy ALL = (root) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/poy

# 升級所有套件
sudo apt-get update && sudo apt-get upgrade

# 如果要安裝 Node.js 8.x 才需要執行以下命令
curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
sudo apt-get install -y nodejs

# 如果要安裝 Node.js 10.x 才需要執行以下命令
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs

# Optional: install build tools
sudo apt-get install -y build-essential

# 升級 npm
sudo npm install -g npm
npm --version
```

## WSL设定Z Shell（zsh）

定义前可以先在Windows系统中安装[Fira Code](https://github.com/tonsky/FiraCode)和[Powerline](https://github.com/powerline/fonts)字型，Powerline我选择Ubuntu Mono的版本。注意！请选择True Type字型（ttf）进行安装。

```
# 下載 zsh
sudo apt-get install zsh
zsh --version

# 將 zsh 設為預設 shell，完成後關掉 App 再重開，並直接按 0 建立空白含註解的 .zshrc
chsh -s $(which zsh)

# 安裝 oh-my-zsh（擇一）
#sh -c "$(wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
# 使用 agnoster 主題
ZSH_THEME="agnoster"

# 將以下設定附加到 .zshrc 檔案後

export TERM="xterm-256color"

# Alias definitions.
# You may want to put all your additions into a separate file like
# ~/.bash_aliases, instead of adding them here directly.
# See /usr/share/doc/bash-doc/examples in the bash-doc package.

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

# ========================================
# Welcome message
# ========================================
eval "$(dircolors ~/.dircolors)";
home
clear
echo -ne "Hello, $USER. Today is, "; date
```

## 调整ls资料夹背景颜色

[是什么导致ls输出中的绿色背景？](https://unix.stackexchange.com/questions/94498/what-causes-this-green-background-in-ls-output?newreg=e23f5b22156d4316a2dd522b69141684)

```
dircolors -p > ~/.dircolors
```

将下面这行

```
OTHER_WRITABLE 34;42 # dir that is other-writable (o+w) and not sticky
```

修改成

```
OTHER_WRITABLE 30;41 # dir that is other-writable (o+w) and not sticky
```

套用变更

```
eval "$(dircolors ~/.dircolors)";
```

如果要之后都套用此设定，可以修改`~/.bashrc`档，在里面执行`eval "$(dircolors ~/.dircolors)";`，让每次启动时，自动套用设定。

![修改前](https://i.imgur.com/nRxt29o.png)

![修改后](https://i.imgur.com/MSpd6xz.png)

## WSL .bashrc设置

原始的`.bashrc`有判断如果家目录下有`.bash_aliases`，并载入该档案内的别名设置，可以加入以下别名：

```
alias home='cd /mnt/c/Users/poypo/'
alias cls=clear
alias e.='explorer.exe .'
alias gl='git log --oneline --all --graph --decorate $*'
alias ll='ls -al --show-control-chars -F --color $*'
```

另外可以在`.bashrc`最后面加上下面的指令，让启动WLS后，会切换到Windows的家目录，并清掉启动过程中的消息，然后显示今天日期。

```
home
clear
echo -ne "Hello, $USER. Today is, "; date
```

## 主题方案

修改Windows Terminal的终端机样式，通过将下面的程序代码加到`profiles.json`中的`schemes`属性，即可使用。

```
{
    "background" : "#073642",
    "black" : "#073642",
    "blue" : "#268BD2",
    "brightBlack" : "#002B36",
    "brightBlue" : "#839496",
    "brightCyan" : "#93A1A1",
    "brightGreen" : "#586E75",
    "brightPurple" : "#6C71C4",
    "brightRed" : "#CB4B16",
    "brightWhite" : "#FDF6E3",
    "brightYellow" : "#657B83",
    "cyan" : "#2AA198",
    "foreground" : "#FDF6E3",
    "green" : "#257387",
    "name" : "PoyChang Dark Theme",
    "purple" : "#D33682",
    "red" : "#D30102",
    "white" : "#EEE8D5",
    "yellow" : "#B58900"
}
```