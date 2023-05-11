FROM ubuntu:21.10

ENV DEBIAN_FRONTEND=noninteractive 

WORKDIR /home/ctf

RUN ln -snf /usr/share/zoneinfo/$CONTAINER_TIMEZONE /etc/localtime && echo $CONTAINER_TIMEZONE > /etc/timezone

RUN apt-get update && \
      apt-get install -y --no-install-recommends socat

RUN rm -rf /var/lib/apt/lists/* && \
      
      useradd -ms /bin/bash ctf && \

      echo "ctf:XDuCzlPJ1lPRF" | chpasswd 

COPY . /home/ctf/

RUN chmod +x /home/ctf/libc.so.6 && \
      chmod +x /home/ctf/ld-2.24.so && \
      chmod +x /home/ctf/chall && \
      chmod +x /home/ctf/run.sh && \
      chown -R ctf:ctf /home/ctf


USER ctf

ENV PORT=1234

CMD ["/bin/bash", "/home/ctf/run.sh"]

EXPOSE 1234
