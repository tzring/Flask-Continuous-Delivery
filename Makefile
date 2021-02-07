install:
	pip install -r requirements.txt

lint:
	pylint --disable=R,C main.py

test:
	python -m pytest -vv main_test.py

all: install lint test