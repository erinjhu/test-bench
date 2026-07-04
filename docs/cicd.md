## CI/CD Pipeline

### YAML File

```yaml
name: HIL Test Pipeline
on: [push, pull_request]

jobs:

  lint-and-analyze:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      # 1. link for Python
      - run: pip install ruff && ruff check src/ tests/
      # 2. static analysis for C
      - run: sudo apt-get install cppcheck && cppcheck --enable=all src/

  build-and-test:
    needs: lint-and-analyze
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run Tests
        run: pytest
```