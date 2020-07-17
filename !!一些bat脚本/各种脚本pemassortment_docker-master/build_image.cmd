@Echo off
REM robocopy /E /R:0 \\FS3\Releases\HOS\PEM.Assortment\1.0.1.1 .\PEM.Assortment
REM robocopy /r:0 \\10.10.1.199\t$\temp\ . GoodsDB.bacpac
REM robocopy /r:0 \\10.10.1.199\t$\temp\ . UIM.bacpac
REM where docker 查看路径

"C:\Program Files\Docker\Docker\resources\bin\docker" build -t slado/pemassortment:latest --build-arg ver=1.1.0.1 .
rem docker build -t slado/pemassortment:latest .


