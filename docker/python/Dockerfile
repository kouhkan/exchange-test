FROM python:3.7
MAINTAINER amirkouhkan1@gmail.com

RUN pip install --upgrade pip

WORKDIR /app
COPY requirements/base.txt /app
COPY requirements/production.txt /app

RUN pip install --no-cache-dir  -r production.txt
COPY . /app
EXPOSE 8000

COPY ./docker/python/entrypoint.sh /entrypoint.sh
ENTRYPOINT["entrypoint.sh"]
CMD ["gunicorn", "A.wsgi", "-b 0.0.0.0:8000"]
