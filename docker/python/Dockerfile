FROM python:3.7
MAINTAINER amirkouhkan1@gmail.com

RUN pip install --upgrade pip

COPY ../../.. /app
WORKDIR /app

COPY ../../../requirements/base.txt /app
COPY ../../../requirements/production.txt /app

RUN pip install -r production.txt
