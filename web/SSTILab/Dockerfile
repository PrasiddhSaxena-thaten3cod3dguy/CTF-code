FROM python:3.8

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r Application/requirements.txt

RUN python create_db.py

EXPOSE 80

CMD ["./run.sh"]