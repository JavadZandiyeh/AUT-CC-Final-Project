FROM python:3.9.17-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
RUN apk --update add build-base mysql-dev bash
COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["python", "bepa.py"]
