set image=rails
set version=1.0.1
set namespace=mdrewt

docker login
docker tag %image% %namespace%/%image%:%version%
docker push  %namespace%/%image%:%version%
