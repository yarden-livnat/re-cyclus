FROM python:3 as gateway-base

ADD . /app
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt -e .

EXPOSE 5000