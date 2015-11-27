FROM teodorescuserban/lns-base-apache2:latest

MAINTAINER Serban Teodorescu, teodorescu.serban@gmail.com

COPY vhost.tpl /etc/apache2/sites-available/
COPY run_apache /etc/service/apache/run

RUN rm -rf /etc/apache2/sites-enabled/* && \
    touch /etc/apache2/sites-available/vhost.conf && \
    ln -sf /etc/apache2/sites-available/vhost.conf /etc/apache2/sites-enabled/vhost.conf && \
    chmod +x /etc/service/apache/run && \
    /etc/my_init.d/00_regen_ssh_host_keys.sh

EXPOSE 80 443

VOLUME ["/srv/www", "/var/log/apache2"]

CMD ["/sbin/my_init"]
