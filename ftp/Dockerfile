FROM teodorescuserban/lns-base-ftp:latest

MAINTAINER Serban Teodorescu, teodorescu.serban@gmail.com

COPY config_ftp.py run_ftp vsftpd_conf /srv/

RUN mv /srv/run_ftp /etc/service/ftp/run && \
    chmod +x /etc/service/ftp/run && \
    mv /etc/vsftpd.conf /etc/vsftpd.orig && \
    cp -a /srv/vsftpd_conf /etc/vsftpd.conf && \
    mkdir -p /srv/ftp && \
    chown -R ftp:users /srv/ftp && \
    /etc/my_init.d/00_regen_ssh_host_keys.sh

EXPOSE 21

VOLUME ["/srv/www", "/var/log/ftp"]

CMD ["/sbin/my_init"]
