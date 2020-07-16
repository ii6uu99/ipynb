#!/bin/bash

sudo apt-get install -y tmux vim 
#WSL安装tmux  bashrc  vimrc Docker的脚本
echo -e "Setting up WSL dotfiles"

#tmux.conf设置
cat > ~/.tmux.conf <<EOF
# Colored tmux
set -g default-terminal "screen-256color"
set -g history-limit 5000
set -g set-titles on
set-option -g status-position bottom
set-option -g status on
set-option -g status-interval 1
EOF
echo -e ".tmux.conf created."

#vimrc设置
cat > ~/.vimrc <<EOF
vmap <C-c> y:new ~/.vimbuffer<CR>VGp:x<CR> \| :!cat ~/.vimbuffer \| clip.exe <CR><CR>
map <C-v> :r ~/.vimbuffer<CR>
syntax enable
filetype on
filetype indent on
filetype plugin on
set smartindent
set encoding=utf8
set number
set noswapfile
set smarttab
set shiftwidth=2
set tabstop=2
set expandtab
set wrap
set incsearch
set smartcase
set ignorecase
EOF
echo -e ".vimrc created."


echo -e "Setting up Docker."
sudo apt-get update -y
# 安装Docker的软件包依赖关系。 
sudo apt-get install -y \
  apt-transport-https \
  ca-certificates \
  curl \
  software-properties-common

# 下载并添加Docker的官方PGP公钥
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
# 验证指纹
sudo apt-key fingerprint 0EBFCD88
# stable是稳定版
sudo add-apt-repository \
  "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) \
  stable"
# 更新apt软件包列表（用于新的apt仓库）
sudo apt-get update -y
# 安装最新Docker CE.
sudo apt-get install -y docker-ce
# 允许您的用户无需root访问权限即可访问Docker CLI
sudo usermod -aG docker $USER
# 将Docker Compose安装到用户的主目录中
sudo apt install docker-compose
#添加host，连接到桌面docker
echo "export DOCKER_HOST=tcp://localhost:2375" >> ~/.bashrc
source ~/.bashrc

sudo cat > /etc/wsl.conf <<EOF
[automount]
root = /
options = "metadata"
EOF
echo "sudo mount --bind /mnt/c /c" >> ~/.bashrc
source ~/.bashrc
echo -e "Created wsl.conf."
echo -e "FINISHED"
echo -e "Don't forget to run: sudo visudo"
echo -e "Add this line: dan ALL=(root) NOPASSWD: /bin/mount"
docker info
docker-compose --version
echo -e "FINISHED"
