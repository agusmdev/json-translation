#!/bin/bash -e

# Repo root directory
REPO_ROOT_DIR="$(git rev-parse --show-toplevel)"

# Activate the environment before running this

# Lint the entire folder
echo "Running Flake8 linter..."
flake8 "${REPO_ROOT_DIR}/json_translation"

echo "Running MyPy type checking..."
mypy "${REPO_ROOT_DIR}/json_translation"


echo ""
echo "Linter and type checking succesfully completed!"
echo ""
