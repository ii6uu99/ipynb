# stage-docker-volumes-windows
Quick Windows batch script to stage a folder to a docker volume

# But why?
Some companies have restrictive firewall policies in place that restict the ability of Docker for Windows to share local volumes. This script allows you to stage the data you would have shared from your local drive and store it on a docker volume that can be referenced by your container.

# Ok, how do I use it?
The batch script takes 2 parameters:
1. Name of docker volume
2. Path to file or directory to copy to the volume

If you want to copy your `deploy` directory to a volume named `deployment`, you would do this:
```
stage-vol.bat deployment c:\users\username\src\project\
```

You can verify that the file or folder is copied by using this command (launched an Alpine container):
```
docker run --rm -it --name test-volume-transfer -v deployment:/data alpine ls /data
file.name
```
