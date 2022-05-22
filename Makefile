migrate:
	@docker compose run web python manage.py makemigrations
	@docker compose run web python manage.py migrate

setup: migrate
	@echo Create a super user
	@docker compose run web python manage.py createsuperuser

start:
	@docker compose up

console:
	@docker compose run web python manage.py shell

test:
	@poetry run python manage.py test

lint:
	@poetry run flake8 blog

requirements:
	@poetry export -f requirements.txt --output requirements.txt



.PHONY: install setup shell lint test check start