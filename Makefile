.PHONY: install test coverage coverage-html clean lint sync docs docs-clean docker docker-build docker-run

install:
	uv pip install -e ".[dev]"

sync:
	uv sync --dev

test:
	uv run pytest

coverage:
	uv run pytest --cov=noaa --cov-report=term-missing

coverage-html:
	uv run pytest --cov=noaa --cov-report=html
	@echo "Coverage report generated in htmlcov/index.html"

docs:
	@echo "Building documentation..."
	@rm -rf docs/_build
	@uv pip list | grep -q sphinx || (echo "Installing sphinx..." && uv pip install sphinx sphinx-rtd-theme)
	cd docs && uv run python -m sphinx -b html source _build/html
	@echo "Documentation built in docs/_build/html/index.html"

docs-clean:
	rm -rf docs/_build
	@echo "Documentation build directory cleaned"

clean:
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm -rf .coverage
	rm -rf *.egg-info
	rm -rf build
	rm -rf dist
	rm -rf docs/_build
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

lint:
	uv run ruff check src/noaa/
	uv run ruff format --check src/noaa/

lint-fix:
	uv run ruff check --fix src/noaa/
	uv run ruff format src/noaa/

docker:
	@echo "Building Docker image..."
	docker build -t noaa-api:latest .
	@echo "Docker image built successfully"

docker-build:
	@echo "Building Docker image with tag noaa-api:latest"
	docker build -t noaa-api:latest -t noaa-api:$(shell grep version pyproject.toml | head -1 | cut -d'"' -f2) .

docker-run:
	@echo "Running Docker image..."
	docker run --rm noaa-api:latest

docker-shell:
	@echo "Starting interactive shell in Docker container..."
	docker run --rm -it noaa-api:latest python
