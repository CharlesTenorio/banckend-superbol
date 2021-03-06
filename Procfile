release: python manage.py migrate --noinput
web: gunicorn superbol_api.wsgi --log-file -
worker: celery -A superbol_api worker -l info --max-tasks-per-child=1 --concurrency=2
beat: celery -A superbol_api beat --loglevel=INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler &