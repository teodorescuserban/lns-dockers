FROM lnsops/base:latest

MAINTAINER Serban Teodorescu <teodorescu.serban@gmail.com>

ENV LANG=en_US.utf8

RUN apk add --update-cache \
        mariadb \
        mariadb-client \
        && \
    rm -rf /var/cache/apk/*
