.PHONY: migrations migrate

include .env

migrate:
	docker compose exec ${USER_SERVICE_CONTAINER} sh -c "python manage.py migrate"

migrations:
	docker compose exec ${USER_SERVICE_CONTAINER} sh -c "python manage.py makemigrations"

connect-users_db:
	docker compose exec -it ${DATABASE_CONTAINER} psql -U ${DATABASE_USER} -d ${DATABASE_NAME}

ps:
	docker compose ps