FROM ubuntu:18.04
MAINTAINER HackingBrawl "https://hackingbrawl.com"

RUN apt-get update

RUN apt-get install -y sudo
RUN apt-get install -y vsftpd

COPY vsftpd.conf /etc/
COPY vsftpd.chroot_list /etc/
COPY vsftpd /etc/init.d/

RUN chmod +x /etc/init.d/vsftpd

RUN adduser anonymous --force-badname
RUN echo 'anonymous:hrlrbuhij' | sudo chpasswd

COPY stegano.png /home/anonymous/

RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 20
EXPOSE 21

CMD /etc/init.d/vsftpd start