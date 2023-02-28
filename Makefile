up:
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

