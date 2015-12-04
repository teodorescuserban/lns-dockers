FROM teodorescuserban/lns-base:latest

MAINTAINER Serban Teodorescu, teodorescu.serban@gmail.com

RUN apt-get -qq -y update && \
    apt-get install -qq -y \
        apache2 && \
        libapache2-mod-rpaf && \
    apt-get clean && \
    a2enmod proxy_fcgi && \
    mkdir -p mkdir -p /var/run/apache2 && \
    chown -R www-data /var/run/apache2 && \
    echo "ServerName localhost" >> /etc/apache2/apache2.conf && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    mkdir -p /etc/service/apache /srv/www /var/lock/apache2 && \
    echo "#!/bin/bash\nset -e\nrm -f /usr/local/apache2/logs/httpd.pid\nexec apache2 -DFOREGROUND\n" > /etc/service/apache/run && \
    chmod +x /etc/service/apache/run
