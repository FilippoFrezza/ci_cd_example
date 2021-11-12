test:
	pytest

lint:
	flake8 test main.py utils.py
	black test main.py utils.py