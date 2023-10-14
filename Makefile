.PHONY: install virtualenv ipython lint fmt test clean build


install:
	@echo "Installing for dev environment"
	@.venv/bin/python -m pip install -e '.[dev]'


virtualenv:
	@python -m pip -m venv .venv


ipython:
	@.venv/bin/ipython


lint:
	@.venv/bin/pflake8


fmt:
	@.venv/bin/isort app tests
	@.venv/bin/black app tests


test:
	@.venv/bin/pytest -s --forked


clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '__pycache__' -exec rm -rf {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	@rm -rf .cache
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@rm -rf build
	@rm -rf dist
	@rm -rf *.egg-info
	@rm -rf htmlcov
	@rm -rf .tox/
	@rm -rf docs/_build


build:
	@python setup.py sdist bdist_wheel
