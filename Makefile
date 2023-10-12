.PHONY: install
install:
	poetry insatll
	pre-commit install

.coverage:
	poetry run coverage run -m unittest

coverage: .coverage
	jq --arg percent "$$(coverage report --format=total)%" '.message = $$percent' asset/coverage.json > asset/coverage.json.tmp
	mv asset/coverage.json.tmp asset/coverage.json
