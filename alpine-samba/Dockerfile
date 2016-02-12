FROM alpine:latest

COPY smb.conf smbd_run nmbd_run /srv

RUN apk update && \
    apk add samba && \
    rm -rf /var/lib/apk/* && \
    mkdir -p /etc/services.d/smbd /etc/services.d/nmbd /srv/shares /srv/configs && \
    mv smb.conf /etc/samba/ && \
    mv smbd_run /etc/services.d/smbd/run && \
    mv nmbd_run /etc/services.d/nmbd/run && \

EXPOSE 139 445

EXPOSE 137/udp 138/udp

VOLUMES ["/srv/configs", "/srv/shares", "/var/log/samba"]

ENTRYPOINT ["/init"]

CMD []
