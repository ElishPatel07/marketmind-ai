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

docker-up:
	docker compose up -d

docker-down:
	docker compose down

docker-logs:
	docker compose logs -f