FROM teodorescuserban/lns-base:latest

MAINTAINER Serban Teodorescu, teodorescu.serban@gmail.com

RUN apt-get -qq update && \
    apt-get install -qq -y \
        libpam-pwdfile \
        vsftpd \
        lftp && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    install -m 755 -o root -g root -d /var/run/vsftpd && \
    install -m 755 -o root -g root -d /var/run/vsftpd/empty && \
    mkdir -p /etc/service/ftp && \
    echo "#!/bin/sh\nset -e\nexec /usr/sbin/vsftpd\n" >> /etc/service/ftp/run && \
    chmod u+x /etc/service/ftp/run && \
    /etc/my_init.d/00_regen_ssh_host_keys.sh
