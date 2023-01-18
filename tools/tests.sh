#!/bin/bash -e

# Activate the environment
# source tools/environment.sh

# Execute tests
echo "Executing unit tests"
# pytest -rsxX ./tests
pytest -rsxX ./tests --cache-clear  #--cov-report=term --cov-report=html:tests/ --cache-clear

echo ""
echo "All tests passed!"
echo ""
