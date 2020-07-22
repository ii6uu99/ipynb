for cmd in `busybox --list`
do echo @%~dp0\\busybox.exe $cmd %*>$cmd.bat
done
pause

最新busybox下载地址
http://frippery.org/files/busybox/busybox.exe

查看busybox最新的支持命令
busybox --list