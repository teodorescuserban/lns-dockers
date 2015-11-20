FROM teodorescuserban/lns-base:latest

MAINTAINER Serban Teodorescu, teodorescu.serban@gmail.com

RUN apt-get -qq update && \
    apt-get install -qq -y \
        nginx-extras && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    mkdir -p /etc/service/nginx && \
    echo "#!/bin/sh\nset -e\ncd /etc/nginx\nexec /usr/sbin/nginx" >> /etc/service/nginx/run && \
    chmod u+x /etc/service/nginx/run && \
    echo "daemon off;" >> /etc/nginx/nginx.conf && \
    /etc/my_init.d/00_regen_ssh_host_keys.sh
