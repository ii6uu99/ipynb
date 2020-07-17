# connect to running docker container
```powershell
docker exec -ti pemassortment-container cmd 
docker exec -ti pemassortment-container powershell

#IP assortment kontaineru z compose
docker inspect -f "{{ .NetworkSettings.Networks.pemassortment_default.IPAddress }}" pemassortment-container
```
# Chocolatey
Package manager pre windows. Instalacia v dockeri
```
RUN Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
RUN Install-PackageProvider -Name chocolatey -Force

```

# ftp downloader
Pouzil som duck, instalovany cez chocolatey
```
choco install duck -y
duck -d ftp://sk0050p/releases/bos/fcviewer/ .\
```

# Links
[Creating A Docker Containerised Environment For SQL Server and Continuous Integration](https://chrisadkin.io/2017/10/19/creating-a-docker-containerised-environment-for-sql-server-and-continuous-integration/)

[Markdown cheat sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

[Persistent sql containers](https://docs.microsoft.com/en-us/sql/linux/sql-server-linux-configure-docker?view=sql-server-2017#production)

[ASP.NET Core and SQL server demo](https://github.com/twright-msft/mssql-aspnet-docker-demo-app)

[MSSQL docker node demo app](https://github.com/twright-msft/mssql-node-docker-demo-app)