<VirtualHost *:80>
    DocumentRoot /srv/www/${BASE_DIR}/www
    ServerName ${DOMAIN}
    ServerAlias www.${DOMAIN}
    CustomLog /srv/www/${BASE_DIR}/logs/access_log combined
    ErrorLog /srv/www/${BASE_DIR}/logs/error_log
    <Directory "/srv/www/${BASE_DIR}/www">
        Allow from all
        Allowoverride all
        Options -Indexes +FollowSymLinks
        DirectoryIndex index.php index.html
        <IfModule mod_rewrite.c>
            RewriteEngine On
            RewriteBase /srv/www/${BASE_DIR}/www
            RewriteLog /srv/www/${BASE_DIR}/logs/rewrite_log
        </IfModule>
    </Directory>
</VirtualHost>
