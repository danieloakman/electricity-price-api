.PHONY: install install-dev dev format lint test type-check

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
	pytest tests/ -v --cov=main --cov-report=term-missing

type-check:
	mypy main.py tests/ --ignore-missing-imports
