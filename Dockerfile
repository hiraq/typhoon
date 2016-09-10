FROM python:2.7.12-alpine
MAINTAINER hiraq <hrxwan@gmail.com>

RUN apk add --update python python-dev bash gcc build-base && rm -rf /var/cache/apk/*
RUN mkdir /typhoon

COPY . /typhoon/
WORKDIR /typhoon

COPY env.sample .env
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "./main.py"]
