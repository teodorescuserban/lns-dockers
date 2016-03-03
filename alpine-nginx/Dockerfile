FROM teodorescuserban/lns-alpine-base:latest

COPY nginx_run nginx_finish /srv/

RUN apk update && \
    apk add nginx && \
    rm -rf /var/lib/apk/* && \
    mkdir -p /etc/services.d/nginx && \
    mv /srv/nginx_run /etc/services.d/nginx/run && \
    mv /srv/nginx_finish /etc/services.d/nginx/finish

EXPOSE 80 443

ENTRYPOINT ["/init"]

CMD []
