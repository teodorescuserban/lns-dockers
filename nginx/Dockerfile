FROM teodorescuserban/lns-base-nginx:latest

MAINTAINER Serban Teodorescu, teodorescu.serban@gmail.com

COPY run_nginx vhost.tpl /srv/

RUN mv /srv/run_nginx /etc/service/nginx/run && \
    chmod +x /etc/service/nginx/run && \
    touch /etc/nginx/sites-available/vhost && \
    ln -sf /etc/nginx/sites-available/vhost /etc/nginx/sites-enabled/vhost && \
    rm -f /etc/nginx/sites-available/vhost && \
    mv /srv/vhost.tpl /etc/nginx/sites-available/vhost.tpl && \
    /etc/my_init.d/00_regen_ssh_host_keys.sh

#    rm -f /etc/nginx/sites-enabled/* && \

EXPOSE 80 443

VOLUME ["/srv/www", "/var/log/nginx"]

CMD ["/sbin/my_init"]
