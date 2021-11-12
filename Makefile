test:
	pytest

lint:
	flake8 test main.py utils.py
	black --check test main.py utils.py