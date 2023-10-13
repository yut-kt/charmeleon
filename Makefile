.PHONY: install
install:
	poetry insatll
	pre-commit install

.PHONY: coverage
coverage:
	poetry run coverage run -m unittest
	jq --arg percent "$$(coverage report --format=total)%" '.message = $$percent' asset/coverage.json > asset/coverage.json.tmp
	mv asset/coverage.json.tmp asset/coverage.json
