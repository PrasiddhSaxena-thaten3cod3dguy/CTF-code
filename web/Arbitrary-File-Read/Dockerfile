FROM python:3.8
WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN cp /usr/src/app/flag.txt /flag.txt
EXPOSE 1337
CMD ["./run.sh"]