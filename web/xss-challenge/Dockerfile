FROM php:8.0-apache

#Install git and MySQL extensions for PHP

RUN apt-get update && apt-get install -y git
# RUN docker-php-ext-install pdo pdo_mysql mysqli
RUN a2enmod rewrite

COPY src /var/www/html/
EXPOSE 80/tcp
EXPOSE 443/tcp

# CMD /usr/local/apache2/bin/apachectl -D FOREGROUND
