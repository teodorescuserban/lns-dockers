FROM teodorescuserban/lns-base-apache2:latest

MAINTAINER Serban Teodorescu, teodorescu.serban@gmail.com

RUN /etc/my_init.d/00_regen_ssh_host_keys.sh

EXPOSE 80 443

VOLUME ["/srv/www", "/var/log/apache2"]

CMD ["/sbin/my_init"]
