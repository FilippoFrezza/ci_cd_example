testing:
	pytest test 

linting:
	flake8 test main.py utils.py
	black test main.py utils.py