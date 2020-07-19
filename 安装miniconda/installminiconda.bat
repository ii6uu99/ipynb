echo 用360极速浏览器打开清华源的miniconda下载网页
@start "360se.exe" "https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/"

rem@start "chrome.exe" "https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/"

pause
echo 下载完成后安装

echo 更改conda源
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --set show_channel_urls yes

echo 通过conda安装pip更快
conda install pip -y

echo 更改pip源
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U
pip3 config set global.index-url http://mirrors.aliyun.com/pypi/simple
pip3 config set install.trusted-host mirrors.aliyun.com

echo 安装jupyter notebook
pip3 install jupyter notebook -y

pause


