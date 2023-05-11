FROM python:3.8

WORKDIR /usr/src/app

COPY . .

RUN bash dependencies.sh

EXPOSE 80

CMD ["bash", "run.sh"]