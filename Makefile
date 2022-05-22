migrate:
	@poetry run python manage.py makemigrations
	@poetry run python manage.py migrate

setup: migrate
	@echo Create a super user
	@poetry run python manage.py createsuperuser

start:
	@poetry run python manage.py runserver

console:
	@poetry run python manage.py shell

test:
	@poetry run python manage.py test

lint:
	@poetry run flake8 blog



.PHONY: install setup shell lint test check start