server {
    listen 80;
    listen 443 ssl;

    server_name ${DOMAIN} www.${DOMAIN};

    root /var/www/html;

    ssl_certificate /etc/nginx/ssl.crt;
    ssl_certificate_key /etc/nginx/ssl.key;

    location / {
        try_files %uri %uri/ @pass;
    }

    location @pass {
        include /etc/nginx/proxy_params;
        proxy_pass http://${APACHE_ADDR}:${APACHE_PORT};
    }
}
