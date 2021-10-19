web: gunicorn backend.wsgi
release: python manage.py migrate
heroku config:set SECRET_KEY=$(date | md5)