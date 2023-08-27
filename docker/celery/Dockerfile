FROM python:3.11

RUN apt update
RUN apt upgrade -y
RUN apt install librabbitmq-dev -y

RUN pip install --upgrade pip
RUN pip install django==4.2.2
RUN pip install mysqlclient
RUN pip install celery[librabbitmq,redis]

WORKDIR /root/src

ENTRYPOINT celery -A ally worker -l DEBUG
