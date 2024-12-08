.PHONY migrations migrate

include .env

migrate:
	docker compose exec ${USER_SERVICE_CONTAINER} sh -c "python manage.py migrate"

migrations:
	docker compose exec ${USER_SERVICE_CONTAINER} sh -c "python manage.py makemigrations"

connect-user_db:
	docker compose exec -it ${USER_DATABASE_CONTAINER} psql -U ${USER_DATABASE_USER} -d ${USER_DATABASE_NAME}

ps:
	docker compose ps