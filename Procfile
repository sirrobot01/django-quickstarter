release: python manage.py migrate
web: gunicorn -w 3 {{ project_name }}.wsgi --log-file -