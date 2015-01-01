export SECRET_KEY=not-important-for-testing
export DATABASE_URL=sqlite://

.PHONY: test

test:
	flake8 pew/pew --ignore=E124,E501,E127,E128
	coverage run ./pew/manage.py test pew
	coverage report
