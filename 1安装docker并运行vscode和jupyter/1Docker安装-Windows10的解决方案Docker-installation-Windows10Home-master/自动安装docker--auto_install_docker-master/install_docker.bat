copy /Y start_docker.bat "C:\Users\mickey\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\start_docker.bat"
copy /Y start_inference.bat "C:\Users\mickey\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\start_inference.bat"
certutil -addstore "TrustedPublisher" registry.cert 
set file="C:\Program Files\Docker\Docker\Docker for Windows.exe"
if exist %file% (
    echo file is exists
)else (
    "Docker for Windows Installer.exe" install --quiet -Verb RunAs
)
(
echo {  "registry-mirrors": [],  "insecure-registries": [    "124.9.14.15:443"  ],  "debug": true,  "experimental": false}
)>"C:\Users\mickey\.docker\daemon.json"
systeminfo | findstr /l "Hypervisor"
if %errorlevel% == 0 (
   cd C:\Windows\System32
   .\shutdown.exe /r /t 00 
) ELSE (
   DISM /Online /Enable-Feature /All /FeatureName:Microsoft-Hyper-V /Quiet
)
