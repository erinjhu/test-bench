lint:
	.venv/bin/ruff check --fix
	.venv/bin/python -m mypy .

test:
	.venv/bin/pytest tests/

# Run this one command locally
ci-check: lint test