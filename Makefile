# Start FastAPI development server
run:
	uvicorn apps.api.main:app --reload


# Run Ruff linting checks
lint:
	ruff check .


# Format codebase using Ruff formatter
format:
	ruff format .


# Run automated tests
test:
	pytest


# Run linting + tests together
check:
	ruff check . && pytest


# Start Docker infrastructure
docker-up:
	docker compose up -d


# Stop Docker infrastructure
docker-down:
	docker compose down


# Stream Docker logs
docker-logs:
	docker compose logs -f