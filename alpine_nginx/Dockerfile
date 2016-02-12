FROM lns-alpine-base:latest

COPY nginx_run finish /srv 

RUN apk update && \
    apk add nginx && \
    rm -rf /var/lib/apk/* && \
    mkdir -p /etc/services.d/nginx && \
    mv /srv/nginx_run /etc/services.d/nginx && \
    mv /srv/finish /etc/services.d/nginx

EXPOSE 80 443

ENTRYPOINT ["/init"]

CMD []
