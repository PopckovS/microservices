FROM python:3.8
#ENV PYTHONUNBUFFERED 1
#ENV PORT 8000
WORKDIR /usr/src/app
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
#EXPOSE 9006
#RUN python server.py # запуск сервера
#RUN python server.py & # запуск сервера в фоновом режиме
#ENTRYPOINT ['python']
CMD python server.py



#FROM ubuntu:latest
#MAINTAINER Andrey Maksimov 'maksimov.andrei@gmail.com'
#RUN apt-get update -y
#RUN apt-get install -y python-pip python-dev build-essential
#COPY . /app
#WORKDIR /app
#RUN pip install -r requirements.txt
#ENTRYPOINT ['python']
#CMD ['app.py']
