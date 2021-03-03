sudo redis-server --port 6380
celery -A superbol_api worker --loglevel=INFO
celery -A superbol_api beat --loglevel=INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler &
sudo -i -u postgres
psql