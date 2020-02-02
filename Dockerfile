FROM python:3.7-alpine

RUN apk update && \
    apk add \
      bash

RUN mkdir /code

WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/

CMD gunicorn --bind 0.0.0.0:$PORT adder_service.wsgi
