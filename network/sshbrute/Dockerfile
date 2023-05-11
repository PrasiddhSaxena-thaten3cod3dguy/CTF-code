FROM ubuntu:14.04
MAINTAINER HackingBrawl "https://hackingbrawl.com"

RUN apt-get update

RUN apt-get install -y sudo
RUN apt-get install -y openssh-server curl
RUN mkdir /var/run/sshd

RUN adduser brute_user --force-badname
RUN echo 'brute_user:password' | chpasswd

COPY flag.txt /home/brute_user

RUN sed -ri 's/^#?PermitRootLogin\s+.*/PermitRootLogin no/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

RUN mkdir /root/.ssh

RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 22

CMD    ["/usr/sbin/sshd", "-D"]


