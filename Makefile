migrate:
	@poetry run python manage.py migrate

setup: migrate
	@echo Create a super user
	@poetry run python manage.py createsuperuser

shell:
	@poetry run python manage.py shell

start:
	@poetry run python manage.py runserver



.PHONY: install setup shell lint test check start