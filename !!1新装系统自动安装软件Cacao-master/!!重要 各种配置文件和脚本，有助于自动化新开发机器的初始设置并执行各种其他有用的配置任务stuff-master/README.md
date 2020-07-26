1. https://github.com/mwanchap/stuff

    

2. Run 64-bit powershell as admin

3. `Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))`

4. `choco install git -y`

5. `cd ~`

6. `git clone https://github.com/mwanchap/stuff.git`

7. `cd stuff`

8. `git config user.email matt@wanchap.com` (除非这是测试或一次性安装)

9. `./install-scripts/0-Start.ps1`
