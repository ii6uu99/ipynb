set EXTENSION_PATH="%~dp0extensions"
set USER_DATA_PATH="%~dp0user_data"

if not exist %EXTENSION_PATH% (
	mkdir %EXTENSION_PATH%
)
if not exist %USER_DATA_PATH% (
	mkdir %USER_DATA_PATH%
)
start Code.exe --extensions-dir %EXTENSION_PATH% --user-data-dir %USER_DATA_PATH%