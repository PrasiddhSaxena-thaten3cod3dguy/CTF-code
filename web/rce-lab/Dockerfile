FROM python:3.8
WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN apt update && apt install -y dnsutils
EXPOSE 80
CMD ["./run.sh"]