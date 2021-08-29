FROM python:3.8.0-buster
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./Crawler.py /app