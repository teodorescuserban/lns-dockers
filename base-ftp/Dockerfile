FROM teodorescuserban/lns-base:latest

MAINTAINER Serban Teodorescu, teodorescu.serban@gmail.com

RUN apt-get -qq update && \
    apt-get install -qq -y \
        libpam-pwdfile \
        vsftpd && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    mkdir -p /etc/service/ftp && \
    echo "#!/bin/sh\nset -e\nexec /usr/sbin/vsftpd\n" >> /etc/service/ftp/run && \
    chmod u+x /etc/service/ftp/run && \
    /etc/my_init.d/00_regen_ssh_host_keys.sh
