FROM teodorescuserban/lns-base:latest

MAINTAINER Serban Teodorescu, teodorescu.serban@gmail.com

RUN apt-get -qq -y update && \
    apt-get install -qq -y \
        postfix \
        postfix-pcre \
        opendkim \
        opendkim-tools && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
