FROM python:3.8
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/app
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
#CMD ["python", "manage.py", "migrate"]

RUN chmod +x ./docker-entrypoint.sh
ENTRYPOINT [ "./docker-entrypoint.sh" ]

#ENTRYPOINT ["sh", "./docker-entrypoint.sh"]

# Если используем только один сервис, то достаточно запустить этот
# Dockerfile и открыть его порт на хост машину.
# Если мы используем docker-compose то пробрасывать порты мы можем
# в файле самом docker-compose.yml в место проброски в Dockerfile
#EXPOSE 8000

#docker-compose run service_1_main_django python manage.py makemigrations
#docker-compose run service_1_main_django python manage.py migrate
