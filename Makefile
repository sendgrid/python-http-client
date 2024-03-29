.PHONY: venv install test-install test clean nopyc

venv:
	@python --version || (echo "Python is not installed, please install Python 2 or Python 3"; exit 1);
	pip install virtualenv
	virtualenv --python=python venv

install: venv
	. venv/bin/activate; pip install -r requirements.txt

test:
	. venv/bin/activate; python -m unittest discover -v

clean: nopyc
	rm -rf venv

nopyc:
	find . -name \*.pyc -delete
