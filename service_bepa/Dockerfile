FROM python:3.9.17-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python3", "bepa.py"]
