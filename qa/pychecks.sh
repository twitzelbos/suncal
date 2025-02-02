#!/bin/sh

# Fail the whole script if any single line fails
set -e

echo "***** Check formating with black *****"
poetry run black --diff --check .
echo "***** Sort module imports with isort *****"
poetry run isort --check .
echo "***** Check typing with mypy *****"
poetry run mypy --install-types .
echo "***** Lint the codebase *****"
poetry run pylint -E suncal tests
