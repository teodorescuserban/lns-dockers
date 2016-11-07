FROM teodorescuserban/lns-base:latest

MAINTAINER Serban Teodorescu, teodorescu.serban@gmail.com

RUN apt-get -qq -y update && \
    apt-get install -qq -y \
        mariadb \
        mysql-client-5.5 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    mkdir -p /etc/service/mysql /srv/db && \
    echo "#!/bin/bash\nset -e\nexec mysqld_safe\n" > /etc/service/mysql/run && \
    chmod +x /etc/service/mysql/run && \
    sed -i 's/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/' /etc/mysql/my.cnf && \
    sed -i 's/^key_buffer\s*=/key_buffer_size =/'                    /etc/mysql/my.cnf && \
    sed -i 's/^datadir\s*.*/datadir = \/srv\/db/'                    /etc/mysql/my.cnf
