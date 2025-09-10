install:
	pip install --upgrade pip && \
		pip install -r requirements.txt

test:
	python -m pytest python_sector/*.py


format:
	black *.py

lint:
	pylint --disable=R,C,redefined-outer-name python_sector/*.py

all: install lint test format