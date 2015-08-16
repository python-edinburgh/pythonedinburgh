export SECRET_KEY=not-important-for-testing
export DATABASE_URL=sqlite://

.PHONY: test

test:
	flake8 pew/pew --ignore=E124,E501,E127,E128
	./pew/manage.py collectstatic --noinput
	coverage run ./pew/manage.py test pew
	coverage report

.PHONY: clean
clean:
	rm -rf staticfiles .tox
