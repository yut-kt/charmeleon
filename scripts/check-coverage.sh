#!/usr/bin/env bash

if [ "$(jq -r '.message' asset/coverage.json)" != "$(coverage report --format=total)%" ]; then
  echo "coverage does not match" "$(jq -r '.message' asset/coverage.json)" "!=" "$(coverage report --format=total)%"
  echo "Please run 'make coverage' and commit again."
  exit 1;
fi
