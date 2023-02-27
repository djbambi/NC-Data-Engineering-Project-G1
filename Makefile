WD=$(shell pwd)
PYTHONPATH=${WD}
PYTHON_INTERPRETER = python
PIP:=pip


# Setup python virtual environment
create-environment:
	@echo ">>> About to create environment..."
	@echo ">>> check python3 version"
	@$(PYTHON_INTERPRETER) --version;
	$(PIP) install -q virtualenv virtualenvwrapper;
	virtualenv venv --python=$(PYTHON_INTERPRETER);


# Function to activate virtual environment before a command
define execute_in_env
	source venv/bin/activate && $1
endef


# Install dependancies from list in requirements.txt file
requirements: create-environment
	@echo ">>> installing requirements"
	$(call execute_in_env, $(PIP) install -r ./requirements.txt)


# Tests for security, pep8 compliance, and unit-testing
security-test:
	$(call execute_in_env, safety check -r ./requirements.txt)
	$(call execute_in_env, bandit -lll ingestion-lambda/*/*.py)

run-flake:
	$(call execute_in_env, flake8 ./ingestion-lambda)
	$(call execute_in_env, flake8 ./transform-lambda)
	$(call execute_in_env, flake8 ./load-lambda)

unit-test:
	$(call execute_in_env, PYTHONPATH=${PYTHONPATH}/ingestion-lambda pytest ./ingestion-lambda -v)
	$(call execute_in_env, PYTHONPATH=${PYTHONPATH}/transform-lambda pytest ./transform-lambda -v)
	$(call execute_in_env, PYTHONPATH=${PYTHONPATH}/load-lambda pytest ./load-lambda -v)

# Runs all above checks
run-checks: security-test run-flake unit-test