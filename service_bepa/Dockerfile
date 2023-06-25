FROM python:3.9.17-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
RUN pip install requests
RUN pip install pymysql

CMD ["python", "bepa.py"]
