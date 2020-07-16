FROM codercom/code-server:3.4.1

RUN sudo chmod 777 /etc/apt/sources.list

RUN echo "deb http://mirrors.tuna.tsinghua.edu.cn/debian/ buster main contrib non-free" > /etc/apt/sources.list
RUN echo "deb http://mirrors.tuna.tsinghua.edu.cn/debian/ buster-updates main contrib non-free" >>/etc/apt/sources.list
RUN echo "deb http://mirrors.tuna.tsinghua.edu.cn/debian/ buster-backports main contrib non-free" >>/etc/apt/sources.list
RUN echo "deb http://mirrors.tuna.tsinghua.edu.cn/debian-security buster/updates main contrib non-free" >>/etc/apt/sources.list


# 更新
RUN sudo apt-get update

# 设置python开发 
RUN sudo apt-get install python3.7 python3-pip inetutils-ping python3-venv -y
RUN python3.7 -m pip install pip
RUN python3.7 -m pip install wheel
RUN python3.7 -m pip install flake8


#更换pip install的源
RUN pip3 install -U pip
RUN pip3 config set global.index-url http://mirrors.aliyun.com/pypi/simple
RUN pip3 config set install.trusted-host mirrors.aliyun.com

#安装requirements.txt的python库
ADD requirements.txt /home/coder/requirements.txt
RUN pip3 install --upgrade -r /home/coder/requirements.txt
RUN rm /home/coder/requirements.txt

# 安装扩展
RUN code-server --install-extension ms-python.python
RUN code-server --install-extension eamodio.gitlens


# ADD settings.json /home/coder/.local/share/code-server/User/settings.json

# code-server settings
USER coder:coder
COPY --chown=coder:coder settings.json /home/coder/.local/share/code-server/User/settings.json


#http端口。不要直接暴露于公共互联网！ 
EXPOSE 8080
