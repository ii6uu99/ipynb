REM Run it from windows CMD

docker build -t devbox .


REM Output should be something like this:

REM d:\devstation-workspace\projects\docker-devstation>docker build -t devbox .
REM Sending build context to Docker daemon 77.31 kB
REM Step 1/15 : FROM ubuntu:14.04
REM  ---> b969ab9f929b
REM Step 2/15 : MAINTAINER Pawel Panasewicz
REM  ---> Using cache
REM  ---> db5bfaab0e64
REM Step 3/15 : RUN apt-get update -y  && apt-get upgrade -y  && apt-get install -y  apt-transport-https  curl  wget  telnet  vim  openssh-server  npm  firefox  sudo
REM  ---> Using cache
REM  ---> 644e239ec4fd
REM Step 4/15 : RUN curl https://xpra.org/gpg.asc | apt-key add -
REM  ---> Using cache
REM  ---> fc011981f85c
REM Step 5/15 : RUN echo "deb https://xpra.org/ trusty main" > /etc/apt/sources.list.d/xpra.list
REM  ---> Using cache
REM  ---> 571bc6da050f
REM Step 6/15 : RUN apt-get update -y
REM  ---> Using cache
REM  ---> e3c3b061a492
REM Step 7/15 : RUN apt-get upgrade -y
REM  ---> Using cache
REM  ---> cf78b3f1ba8e
REM Step 8/15 : RUN apt-get install -y xpra
REM  ---> Using cache
REM  ---> abc6875920af
REM Step 9/15 : RUN apt-get install -y python-dbus
REM  ---> Using cache
REM  ---> db04fe0b2fc4
REM Step 10/15 : RUN adduser --disabled-password --gecos "" devbox
REM  ---> Using cache
REM  ---> 057184ad5f47
REM Step 11/15 : RUN echo "devbox:asdf"| chpasswd
REM  ---> Using cache
REM  ---> c5c7a82198d2
REM Step 12/15 : RUN useradd -G xpra vivek #add devbox user to xpra group
REM  ---> Using cache
REM  ---> 67f66bfdf776
REM Step 13/15 : RUN mkdir /var/run/sshd
REM  ---> Using cache
REM  ---> 13dc930681f3
REM Step 14/15 : EXPOSE 22
REM  ---> Using cache
REM  ---> bde467423411
REM Step 15/15 : CMD /usr/sbin/sshd -D
REM  ---> Using cache
REM  ---> bc4cdc4b79a8
REM Successfully built bc4cdc4b79a8
REM SECURITY WARNING: You are building a Docker image from Windows against a non-Windows Docker host. All files and directories added to build context will have '-rwxr-xr-x' permissions. It is recommended to double check and reset permissions for sensitive files and directories.
