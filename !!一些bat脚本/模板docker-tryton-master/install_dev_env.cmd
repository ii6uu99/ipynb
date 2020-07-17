docker pull jenkinsci/blueocean
docker pull docker:dind

docker network create jenkins

docker volume create jenkins-docker-certs
docker volume create jenkins-data


(
echo FROM jenkinsci/blueocean
echo USER root
echo RUN apk update
echo RUN apk add python python-dev py-pip build-base libffi-dev openssl-dev gcc libc-dev make autoconf automake libtool jq
echo RUN pip install docker-compose
echo RUN pip install ecscli
echo RUN pip install awscli
echo RUN apk add groff
) > temp.Dockerfile

docker build - < temp.Dockerfile -t jhg_jenkins

del temp.Dockerfile

docker container run --name jenkins-docker --rm --detach ^
  --privileged --network jenkins --network-alias docker ^
  --env DOCKER_TLS_CERTDIR=/certs ^
  --volume jenkins-docker-certs:/certs/client ^
  --volume jenkins-data:/var/jenkins_home ^
  --publish 8000:8000 --publish 3001:3001 docker:dind
  
docker container run --name jenkins-blueocean --rm --detach ^
  --network jenkins --env DOCKER_HOST=tcp://docker:2376 ^
  --env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=0 ^
  --volume jenkins-data:/var/jenkins_home ^
  --volume jenkins-docker-certs:/certs/client:ro ^
  --publish 1000:8080 --publish 50000:50000 jhg_jenkins