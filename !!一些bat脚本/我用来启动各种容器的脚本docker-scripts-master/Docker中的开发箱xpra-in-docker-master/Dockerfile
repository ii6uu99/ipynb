FROM ubuntu:14.04
MAINTAINER Pawel Panasewicz

RUN apt-get update -y \
 && apt-get upgrade -y \
 && apt-get install -y \
 apt-transport-https \
 curl \
 wget \
 telnet \
 vim \
 openssh-server \
 npm \
 firefox \
 sudo

#xpra and it's dependencies
RUN curl https://xpra.org/gpg.asc | apt-key add -
RUN echo "deb https://xpra.org/ trusty main" > /etc/apt/sources.list.d/xpra.list
RUN apt-get update -y \
 && apt-get upgrade -y \
 && apt-get install -y \
 xpra \
 python-dbus \
 Xorg \
 dbus-x11 \
 xserver-xorg-video-dummy

RUN mkdir -p /var/run/xpra
RUN chown :xpra /var/run/xpra
RUN chmod g+w /var/run/xpra

# Upstart and DBus have issues inside docker. We work around in order to install firefox.
#(Roberto G. Hashioka - docker-desktop)
RUN dpkg-divert --local --rename --add /sbin/initctl && ln -sf /bin/true /sbin/initctl


#create user devbox with password asdf
RUN adduser --disabled-password --gecos "" devbox
RUN echo "devbox:asdf"| chpasswd
RUN usermod -a -G sudo,xpra,tty,video,dialout  devbox #add devbox user to groups

#run ssh service
RUN mkdir /var/run/sshd
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
