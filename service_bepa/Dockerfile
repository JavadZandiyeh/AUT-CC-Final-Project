FROM python:3.9.17-alpine AS builder

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
RUN apk --update add build-base mysql-dev bash
COPY requirements.txt .
RUN pip install -r requirements.txt

FROM python:3.9.17-alpine AS final

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages

WORKDIR /app

CMD ["python", "bepa.py"]
