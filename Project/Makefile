include ./.env

.PHONY: run-services connect-db migrate migrations migrate-all

connect-db:
	docker compose exec -it ${DATABASE_HOST} psql -U ${DATABASE_USER} -d ${DATABASE_NAME}

migrate:
ifndef PROJECT
	@echo "Invalid project name. Please specify PROJECT."
else
	docker compose exec $(PROJECT) python manage.py migrate $(APP) --fake-initial
endif

migrations:
ifndef PROJECT
	@echo "Invalid project name. Please specify PROJECT."
else
ifndef APP
	@echo "Invalid app name. Please specify APP."
else
	docker compose exec $(PROJECT) python manage.py makemigrations $(APP)
endif
endif

migrate-all:
	make migrate PROJECT=user_service APP=user_app
	make migrate PROJECT=auth_service APP=auth_app
	make migrate PROJECT=user_service
	make migrate PROJECT=auth_service
