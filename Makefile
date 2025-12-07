.PHONY: install test coverage coverage-html clean lint sync docs docs-clean

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
