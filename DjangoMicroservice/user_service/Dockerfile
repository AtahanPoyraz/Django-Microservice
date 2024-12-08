FROM python:3.13

WORKDIR /app

COPY user_service/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY user_service/ /app/

CMD ["sh", "-c", "python manage.py wait_for_db && python manage.py runserver 0.0.0.0:8001"]