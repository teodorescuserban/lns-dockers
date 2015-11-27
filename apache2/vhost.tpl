<VirtualHost *:80>
    DocumentRoot /srv/www
    ServerName ${DOMAIN}
    ServerAlias www.${DOMAIN}
    CustomLog /srv/logs/access_log combined
    ErrorLog /srv/logs/error_log

    ProxyPassMatch ^/(.*\.php(/.*)?)$ fcgi://${FPM_ADDR}:${FPM_PORT}/srv/www/$1

    <Directory "/srv/www">
        Allow from all
        Allowoverride all
        Require all granted
        Options -Indexes +FollowSymLinks
        DirectoryIndex index.php index.html
        <IfModule mod_rewrite.c>
            RewriteEngine On
            RewriteBase /srv/www
            RewriteLog /srv/logs/rewrite_log
        </IfModule>
    </Directory>
</VirtualHost>
