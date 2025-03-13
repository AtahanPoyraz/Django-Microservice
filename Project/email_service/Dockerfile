FROM --platform=$BUILDPLATFORM python:3.12 AS builder

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . /app/

CMD ["sh", "-c", "celery -A email_app.tasks worker --loglevel=info & python manage.py runserver 0.0.0.0:8002"]
