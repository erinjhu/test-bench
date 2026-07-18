## CI/CD Pipeline

### Mypy Static Type Checking

#### What it does
- Add and check type hints to make code cleaner
- Flags types mismatches

#### Benefits
- More readable; can show types in the function signatures
- Refactoring; when changing a data structure, you can find all the places in the code that the change affects

#### How to use

### Ruff Linter



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