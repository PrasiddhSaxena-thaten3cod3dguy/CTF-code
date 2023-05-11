FROM ubuntu:20.04

# Updating the instance
RUN apt-get update

# Installing apt dependencies
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get install -y python3 python3-pip apache2 libapache2-mod-wsgi-py3 sudo whois

# Installing flask and dependencies
RUN pip install flask numpy pandas

# Creating users
RUN useradd -ms /bin/bash trunks
RUN echo "trunks:ghtnqfr" | chpasswd

# Copying source files to docker
COPY . /var/www/html

# Moving flag
RUN mv /var/www/html/flag.txt /root/flag.txt
RUN chown root:root /root/flag.txt
RUN chmod 700 /root/flag.txt

# Moving iso file
RUN mv /var/www/html/backup.iso /opt/backup.iso
RUN chmod 644 /opt/backup.iso
RUN echo 'trunks ALL=(ALL) NOPASSWD: /usr/bin/python3 /home/trunks/fun.py' >> /etc/sudoers
RUN mv /var/www/html/fun.py /home/trunks/fun.py
RUN chmod 644 /home/trunks/fun.py

# Configuring apache
RUN mv /var/www/html/whoisapp.conf /etc/apache2/sites-available/whoisapp.conf
RUN rm /etc/apache2/sites-enabled/000-default.conf
RUN a2ensite whoisapp

CMD ["apache2ctl", "-D", "FOREGROUND"]