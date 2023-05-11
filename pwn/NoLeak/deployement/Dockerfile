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

RUN chmod +x /home/ctf/* && \
      chown -R ctf:ctf /home/ctf


USER ctf

ENV PORT=9856

CMD ["/bin/bash", "/home/ctf/run.sh"]

EXPOSE 9856
