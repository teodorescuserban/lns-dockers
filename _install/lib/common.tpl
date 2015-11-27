# 2015 copyleft Serban Teodorescu 

nginx:
  hostname: nginx
  restart: always
  image: ${BASE_IMG}nginx:latest
  env_file:
    - env_common

apache:
  hostname: apache
  restart: always
  image: ${BASE_IMG}apache2:latest
  volumes:
    - ${VOL_SITE}:/srv/www
    - ${VOL_SITE_LOGS}:/srv/logs
  ports:
    - "${WB_ADDR}:${APACHE_HTTP_PORT}:80"
    - "${WB_ADDR}:${APACHE_HTTPS_PORT}:443"
  env_file:
    - env_common
    - env_apache
    - env_fpm
  environment:
    - VIRTUAL_HOST=${DOMAIN},www.${DOMAIN}

fpm:
  hostname: fpm
  restart: always
  image: ${BASE_IMG}fpm:latest
  volumes:
    - ${VOL_SITE}:/srv/www
    - ${VOL_SITE_LOGS}:/srv/logs
  ports:
    - "${WB_ADDR}:${FPM_PORT}:9000"
  env_file:
    - env_common
    - env_mysql
    - env_mysql_prv

mysql:
  hostname: mysql
  restart: always
  image: ${BASE_IMG}mysql:latest
  volumes:
    - ${VOL_DB}:/srv/db
  ports:
    - "${DB_ADDR}:${MYSQL_PORT}:3306"
  env_file:
    - env_common
    - env_mysql_prv
    - env_mysql_prv_root
