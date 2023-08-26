FROM python:3.11

RUN apt update
RUN apt upgrade -y
RUN pip install --upgrade pip
RUN pip install django==4.2.2
RUN pip install mysqlclient
WORKDIR /root/src/

# ENTRYPOINT sleep infinity
ENTRYPOINT python manage.py runserver 0.0.0.0:8000
