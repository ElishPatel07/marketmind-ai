run:
	uvicorn apps.api.main:app --reload

lint:
	ruff check .

format:
	ruff format .

test:
	pytest

check:
	ruff check . && pytest