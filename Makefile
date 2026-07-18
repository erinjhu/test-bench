lint:
	ruff check --fix
	python -m mypy .

test:
	pytest tests/

# Run this one command locally
ci-check: lint test