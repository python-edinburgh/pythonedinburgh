# web: python pew/manage.py runserver --settings=pew.settings 0.0.0.0:$PORT
web: gunicorn pew.wsgi --log-file - --chdir pew
