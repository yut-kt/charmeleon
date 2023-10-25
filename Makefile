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

.PHONY: go-build
go-build: # Only works on mac. Need to install go.
	CGO_ENABLED=1 GOOS=darwin GOARCH=amd64 go build -C libs/go -buildmode=c-shared -o ../../charmeleon/go/darwin_amd64 main.go
	CGO_ENABLED=1 GOOS=darwin GOARCH=arm64 go build -C libs/go -buildmode=c-shared -o ../../charmeleon/go/darwin_arm64 main.go
	docker run --rm -v "${PWD}:/go/src" --platform linux/amd64 golang:latest bash -c "CGO_ENABLED=1 GOOS=linux GOARCH=amd64 go build -C src/libs/go -buildmode=c-shared -o ../../charmeleon/go/linux_amd64 main.go"
	docker run --rm -v "${PWD}:/go/src" --platform linux/arm64 golang:latest bash -c "CGO_ENABLED=1 GOOS=linux GOARCH=arm64 go build -C src/libs/go -buildmode=c-shared -o ../../charmeleon/go/linux_arm64 main.go"
