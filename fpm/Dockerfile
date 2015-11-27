FROM teodorescuserban/lns-base-fpm:latest

MAINTAINER Serban Teodorescu, teodorescu.serban@gmail.com

COPY run_fpm php-fpm.conf www.conf test.php add_a_blank_wordpress.sh /srv/

RUN sed -i 's/.*date.timezone =.*/date\.timezone = UTC/'                 /etc/php5/fpm/php.ini && \
    sed -i 's/.*error_log =.*/error_log = syslog/'                       /etc/php5/fpm/php.ini && \
    sed -i 's/.*cgi.fix_pathinfo=.*/cgi.fix_pathinfo=0/'                 /etc/php5/fpm/php.ini && \
    sed -i -e "s/upload_max_filesize\s*=.*/upload_max_filesize = 100M/g" /etc/php5/fpm/php.ini && \
    sed -i -e "s/post_max_size\s*=.*/post_max_size = 100M/g"             /etc/php5/fpm/php.ini && \
    echo "alias mysql='mysql -h ${MYSQL_ADDR} -P ${MYSQL_PORT} -u ${MYSQL_USER} -p ${MYSQL_DB}'" > /root/.bash_aliases && \
    mv /etc/php5/fpm/php-fpm.conf /etc/php5/fpm/php-fpm.orig && \
    mv /etc/php5/fpm/pool.d/www.conf /etc/php5/fpm/pool.d/www.orig && \
    mv /srv/php-fpm.conf /etc/php5/fpm/ && \
    mv /srv/www.conf /etc/php5/fpm/pool.d/ && \
    mv /srv/run_fpm /etc/service/fpm/run && \
    mkdir -p /chroot/srv/www /srv /srv/logs && \
    ln -sf /chroot/srv/www /srv/www && \
    chmod +x /etc/service/fpm/run

EXPOSE 9000

RUN /etc/my_init.d/00_regen_ssh_host_keys.sh

CMD ["/sbin/my_init"]
