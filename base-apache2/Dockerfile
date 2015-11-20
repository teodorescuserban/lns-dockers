FROM teodorescuserban/lns-base:latest

MAINTAINER Serban Teodorescu, teodorescu.serban@gmail.com

RUN apt-get -qq -y update && \
    apt-get install -qq -y \
        apache2 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    mkdir -p /etc/service/apache2 /srv/www && \
    echo "#!/bin/bash\nset -e\nrm -f /usr/local/apache2/logs/httpd.pid\nexec httpd -DFOREGROUND\n" > /etc/service/apache2/run && \
    chmod +x /etc/service/apache2/run
