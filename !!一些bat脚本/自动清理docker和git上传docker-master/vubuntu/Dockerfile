FROM ubuntu

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y sudo nano python python-pip python-dev build-essential

RUN sudo pip install --upgrade pip && sudo pip install --upgrade virtualenv

COPY scripts/ /usr/scripts/

CMD ["/bin/bash"]
