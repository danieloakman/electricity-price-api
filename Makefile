.PHONY: install install-dev dev format lint test type-check up down logs build

install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt

dev:
	uvicorn main:app --host 0.0.0.0 --port 8000 --reload

format:
	black .

lint:
	flake8 *.py tests/*.py

test:
	PYTHONPATH=. pytest tests/ -v --cov=main --cov-report=term-missing

type-check:
	mypy *.py tests/*.py --ignore-missing-imports

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs -f