FROM python:3.9.17-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

USER root

WORKDIR /app

COPY requirements.txt /app

RUN apk --update add build-base mysql-dev bash
RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE ${APP_PORT}

WORKDIR /app/project_peyk

ENTRYPOINT ["/bin/bash", "entrypoint.sh"]
