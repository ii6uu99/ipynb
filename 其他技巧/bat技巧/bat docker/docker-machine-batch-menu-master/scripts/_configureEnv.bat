echo ...... Configuring environment variables for docker-machine
docker-machine env --shell cmd %MACHINE_NAME% >> %ENV_CONFIGURE_BATCH_FILE%
call %ENV_CONFIGURE_BATCH_FILE%
echo ...... Done!