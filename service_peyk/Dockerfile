FROM python:3.9.17-alpine AS builder

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN apk --update add build-base mysql-dev bash
RUN pip3 install -r requirements.txt

FROM python:3.9.17-alpine AS final

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=builder /usr/lib/libmariadb.so.3 /usr/lib/
COPY --from=builder /usr/lib/mariadb/plugin/caching_sha2_password.so /usr/lib/mariadb/plugin/

EXPOSE ${APP_PORT}

WORKDIR /app/project_peyk

ENTRYPOINT ["/bin/sh", "entrypoint.sh"]
