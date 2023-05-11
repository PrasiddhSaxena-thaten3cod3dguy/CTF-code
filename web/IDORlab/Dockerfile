FROM python:3.8
WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN python lipsum.py
RUN mv 23-11-21.txt Application/static/reports_gvrb/23-11-21.txt
EXPOSE 80
CMD ["./run.sh"]