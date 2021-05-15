FROM python:3.7-alpine:3.10
ENV PYTHONUNBUFFERED 1

RUN apt-get update

RUN apt-get install gcc libc-dev libffi-dev software-properties-common python3-pip -y
COPY ./requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt

RUN mkdir /app
WORKDIR /app
COPY . /app

RUN chmod -R 777 /app