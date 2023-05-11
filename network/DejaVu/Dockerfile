FROM ubuntu:20.04

# Updates and dependencies
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get install -y python3 python3-pip apache2 libapache2-mod-wsgi-py3 sudo vim
RUN pip install flask numpy pandas

# Moving source files
COPY . /var/www/dejavu
RUN mv /var/www/dejavu/dejavu.conf /etc/apache2/sites-available/dejavu.conf
RUN mv /var/www/dejavu/ports.conf /etc/apache2/ports.conf

# Configuring user
RUN useradd -ms /bin/bash saitama
RUN echo "saitama:zxFrFeAghitVekjzZyFQhEHDYiAXlSaR" | chpasswd
RUN gcc /var/www/dejavu/test.c -o /home/saitama/test
RUN chown 'saitama:saitama' /home/saitama/test
RUN chmod +x /home/saitama/test
RUN echo 'www-data ALL=(saitama) NOPASSWD: /home/saitama/test' >> /etc/sudoers
RUN rm /var/www/dejavu/test.c

# Configuring root user
RUN echo "root:cYubwmWZkwEZdkfcgtyQGnatkQmyXvHz" | chpasswd
RUN mv /var/www/dejavu/pwd.txt /root/pwd.txt
RUN chown 'root:root' /root/pwd.txt
RUN chmod 600 /root/pwd.txt
RUN mv /var/www/dejavu/test.sh /opt/test.sh
RUN chown 'root:root' /opt/test.sh
RUN chmod 755 /opt/test.sh
RUN echo 'saitama ALL=(ALL) NOPASSWD: /opt/test.sh' >> /etc/sudoers

# Moving flag
RUN mv /var/www/dejavu/flag.txt /root/flag.txt
RUN chown 'root:root' /root/flag.txt
RUN chmod 600 /root/flag.txt

# Enabling site
RUN a2ensite dejavu
CMD ["apache2ctl", "-D", "FOREGROUND"]