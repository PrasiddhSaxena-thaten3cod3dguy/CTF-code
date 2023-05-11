FROM ubuntu:20.04

# Updates and dependencies
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get install -y python3 python3-pip apache2 libapache2-mod-wsgi-py3 sudo libcap2-bin
RUN pip install flask numpy pandas

# Moving source files
COPY . /var/www
RUN mv /var/www/aacharpapad.conf /etc/apache2/sites-available/aacharpapad.conf
RUN mv /var/www/ports.conf /etc/apache2/ports.conf

# Configuring system users
RUN useradd -ms /bin/bash sonu
RUN echo 'sonu:T4pu_s3n4_002' | chpasswd 
RUN mv /var/www/encrypt.py /home/sonu/encrypt.py
RUN mv /var/www/out.txt /home/sonu/out.txt
RUN chmod 644 /home/sonu/encrypt.py
RUN chmod 644 /home/sonu/out.txt
RUN chown 'sonu:sonu' /home/sonu/encrypt.py
RUN chown 'sonu:sonu' /home/sonu/out.txt
RUN echo 'sonu ALL=(ALL) NOPASSWD: /usr/bin/id' >> /etc/sudoers
RUN mv /var/www/flag.txt /root/flag.txt
RUN chmod 444 /root/flag.txt
RUN chown 'root:root' /root/flag.txt
RUN chmod +s /usr/sbin/capsh

# Enabling site
RUN a2ensite aacharpapad
CMD ["apache2ctl", "-D", "FOREGROUND"]