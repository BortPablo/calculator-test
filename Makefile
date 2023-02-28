TITLE:="Makefile for simple calculator"

info:
	@echo $(TITLE)
	@echo "=============================="
	@echo "make setup        - Create virtual environment and install dependencies"
	@echo "make requirements - Create requirements.txt"
	@echo "make clean        - Remove virtual environment and create requirements.txt"
	@echo "make test         - Run tests"
	@echo "make calculator   - Run calculator"

setup:
	@echo "Creating virtual environment..."
	python3 -m virtualenv venv
	@echo "Installing dependencies..."
	venv/bin/pip install -r requirements.txt
	@echo "Starting VSCode..."
	code .

requirements:
	@echo "Creating requirements.txt..."
	venv/bin/pip freeze > requirements.txt

clean: requirements
	@echo "Removing virtual environment..."
	rm -rf ./src/__pycache__
	rm -rf venv

test:
	@echo "Running tests..."
	venv/bin/python ./tests/simple_calculator_tests.py
	venv/bin/python ./tests/medium_calculator_tests.py

calculator:
	@echo "Running calculator..."
	venv/bin/python ./src/medium_calculator.py
