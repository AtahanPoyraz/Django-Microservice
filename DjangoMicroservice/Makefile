include .env

migrate:
	docker compose exec ${API_GATEWAY_CONTAINER} sh -c "python manage.py migrate"
	docker compose exec ${USER_SERVICE_CONTAINER} sh -c "python manage.py migrate"
	docker compose exec ${AUTH_SERVICE_CONTAINER} sh -c "python manage.py migrate"
	docker compose exec ${EMAIL_SERVICE_CONTAINER} sh -c "python manage.py migrate"

migrations:
	docker compose exec ${API_GATEWAY_CONTAINER} sh -c "python manage.py makemigrations"
	docker compose exec ${USER_SERVICE_CONTAINER} sh -c "python manage.py makemigrations"
	docker compose exec ${AUTH_SERVICE_CONTAINER} sh -c "python manage.py makemigrations"
	docker compose exec ${EMAIL_SERVICE_CONTAINER} sh -c "python manage.py makemigrations"

connect-db:
	docker compose exec -it ${DATABASE_CONTAINER} psql -U ${DATABASE_USER} -d ${DATABASE_NAME}