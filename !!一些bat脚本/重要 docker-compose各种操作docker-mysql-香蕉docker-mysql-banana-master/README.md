# docker-mysql-banana

* mysql 8

You can connect directly to mysql by docker-compose up.

Please use "docker-compose-up.bat" when starting.

Please use "docker-compose-down.bat" when stopping.

```
version: '2'
services:
  db:
    image: mysql:8
    command: --default-authentication-plugin=mysql_native_password
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: example
      MYSQL_DATABASE: banana
      MYSQL_USER: develop
      MYSQL_PASSWORD: develop
    ports:
      - 33306:3306
```
