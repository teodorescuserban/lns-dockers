FROM teodorescuserban/lns-base:latest

MAINTAINER Serban Teodorescu, teodorescu.serban@gmail.com

RUN apt-get -qq -y update && \
    apt-get install -qq -y \
        php5 \
        php5-mysql \
        mysql-client-5.5 \
        php5-fpm && \
    apt-get clean && \
    mkdir -p /etc/service/fpm

#    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
