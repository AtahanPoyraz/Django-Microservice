FROM --platform=$BUILDPLATFORM python:3.12 AS builder

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN python manage.py makemigrations user_app

CMD ["sh", "-c", "python manage.py wait_for_db && python manage.py runserver 0.0.0.0:8000"]
