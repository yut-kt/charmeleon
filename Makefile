.PHONY: install
install:
	python -m pip install --upgrade setuptools pip poetry
	python -m poetry install
	pre-commit install

.PHONY: coverage
coverage:
	poetry run coverage run -m unittest
	jq --arg percent "$$(coverage report --format=total)%" '.message = $$percent' asset/coverage.json > asset/coverage.json.tmp
	mv asset/coverage.json.tmp asset/coverage.json
