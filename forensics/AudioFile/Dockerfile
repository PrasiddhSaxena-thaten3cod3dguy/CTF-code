FROM python:3.8
WORKDIR /usr/src/app
COPY . .
RUN pip install flask numpy pandas pyjwt
EXPOSE 1337
CMD ["python", "app.py"]
