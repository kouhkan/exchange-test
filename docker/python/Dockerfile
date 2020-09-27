FROM python:3.7
MAINTAINER amirkouhkan1@gmail.com

RUN pip install --upgrade pip

WORKDIR /app
COPY requirements/base.txt /app
COPY requirements/production.txt /app

RUN pip install --no-cache-dir  -r production.txt
COPY . /app


EXPOSE 8000