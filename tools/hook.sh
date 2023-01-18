#!/bin/bash -e
REPO_ROOT_DIR="$(git rev-parse --show-toplevel)"

# PEP8 Linter validator
echo ""
echo "Checking Code Style: "
echo ""
${REPO_ROOT_DIR}/tools/lint.sh || { echo "You have style errors, fix them before the commit"; exit 1; }

# Test the App
echo ""
echo "Running Tests: "
echo ""
${REPO_ROOT_DIR}/tools/tests.sh unit || { echo "You have test errors, fix them before the commit"; exit 1; }
