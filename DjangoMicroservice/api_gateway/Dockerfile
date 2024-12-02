FROM python:3.13

WORKDIR /app

COPY api_gateway/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY api_gateway/ /app/

CMD ["sh", "-c", "python manage.py wait_for_db && python manage.py runserver 0.0.0.0:8000"]