rem Startup OpenVas container
rem Host: https://localhost
rem Port:443 for Access
rem Port:9390 for Management
docker run -d -p 443:443 -p 9390:9390 -v ./data:/var/lib/openvas/mgr/ --name openvas mikesplain/openvas:9
