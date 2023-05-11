FROM ubuntu:20.04

# Updates and dependencies
ARG DEBIAN_FRONTEND=noninteractive
RUN apt update
RUN apt-get install -y python3 python3-pip apache2 libapache2-mod-wsgi-py3 sudo policykit-1
RUN pip install flask numpy pandas pyjwt

# Moving source files
COPY . /var/www/unpredictable
RUN mv /var/www/unpredictable/unpredictable.conf /etc/apache2/sites-available/unpredictable.conf
RUN mv /var/www/unpredictable/ports.conf /etc/apache2/ports.conf

# Configuring root user
RUN mv /var/www/unpredictable/pkexec /usr/bin/pkexec
RUN chmod +s /usr/bin/pkexec

# Moving flag
RUN mv /var/www/unpredictable/flag.txt /root/flag.txt
RUN chown 'root:root' /root/flag.txt
RUN chmod 600 /root/flag.txt

# Enabling site
RUN a2ensite unpredictable
CMD ["apache2ctl", "-D", "FOREGROUND"]