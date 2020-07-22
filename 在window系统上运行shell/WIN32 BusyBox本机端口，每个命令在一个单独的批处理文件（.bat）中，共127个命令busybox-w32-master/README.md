https://github.com/witwall/busybox-w32



* \## About这不是https://github.com/rmyorston/busybox-w32的分支，而是帮助项目。

    busybox-w32有127个命令，

    ```
           [, [[, ar, ash, awk, base64, basename, bash, bbconfig, bunzip2, bzcat,
           bzip2, cal, cat, catv, chmod, cksum, clear, cmp, comm, cp, cpio, cut,
           date, dc, dd, df, diff, dirname, dos2unix, dpkg-deb, du, echo, ed,
           egrep, env, expand, expr, false, fgrep, find, fold, ftpget, ftpput,
           getopt, grep, groups, gunzip, gzip, hd, head, hexdump, id, ipcalc,
           kill, killall, less, ln, logname, ls, lzcat, lzma, lzop, lzopcat, man,
           md5sum, mkdir, mktemp, mv, nc, od, patch, pgrep, pidof, printenv,
           printf, ps, pwd, rev, rm, rmdir, rpm2cpio, sed, seq, sh, sha1sum,
           sha256sum, sha3sum, sha512sum, shuf, sleep, sort, split, stat, strings,
           sum, tac, tail, tar, tee, test, touch, tr, true, truncate, uname,
           uncompress, unexpand, uniq, unix2dos, unlink, unlzma, unlzop, unxz,
           unzip, usleep, uudecode, uuencode, vi, wc, wget, which, whoami, xargs,
           xz, xzcat, yes, zcat
    ```

    如果您不想以这种方式运行命令

    ```
    cmd.exe /c C:\path\to\busybox.exe sh -l
    ```

    但

    ```
    sh -l
    ```

    这个项目适合你

    \## Update busybox.exe这是最新版本[busybox.exe](http://frippery.org/files/busybox/busybox.exe)

    \## script创建127个批处理文件

    *在Linux下

    ```
    sed -r  's/\ *(\w*\[*\-*\w*),*/echo @%~dp0\\\\busybox.exe \1 %*>\1.bat\n/g' bb.txt>bb
    chmod u+x bb
    ./bb
    zip busybox.zip *.bat
    ```

    *在Windows下，

    ```
    busybox bash
    $ for cmd in `busybox --list`; do echo @%~dp0\\busybox.exe $cmd %*>$cmd.bat ;done
    ```

    \##更改日志

    - 用[wget.exe](https://eternallybored.org/misc/wget/current/wget.exe)替换busybox wget 以支持HTTPS

    \## PS

    - [scoop](https://github.com/lukesampson/scoop)是一个很好的项目，但是取决于PowerShell3
    - [gow](https://github.com/bmatzelle/gow)（Windows上的Gnu）是Cygwin的轻量级替代品