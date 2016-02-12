FROM teodorescuserban/lns-alpine-base:latest

COPY smb.conf smbd_run nmbd_run /srv/

RUN apk update && \
    apk add samba && \
    rm -rf /var/lib/apk/* && \
    mkdir -p /etc/services.d/smbd /etc/services.d/nmbd /srv/shares /srv/configs && \
    mv /srv/smb.conf /etc/samba/ && \
    mv /srv/smbd_run /etc/services.d/smbd/run && \
    mv /srv/nmbd_run /etc/services.d/nmbd/run && \

EXPOSE 139 445

EXPOSE 137/udp 138/udp

VOLUME ["/srv/configs", "/srv/shares", "/var/log/samba"]

ENTRYPOINT ["/init"]

CMD []
