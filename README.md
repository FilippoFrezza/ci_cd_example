# ci_cd_example

Best practices to take into account:
1. Github actions on push & pull_request --> .git/workflows/ci_cd.yml file
2. Makefile
3. test folder
4. pre-commit-config.yml (linting prior to any commit)- ```pre-commit install``` run this command once you've generated the pre-commit-config.yml file
5. main branch rule (under settings- branches) - only merge is status check is == success