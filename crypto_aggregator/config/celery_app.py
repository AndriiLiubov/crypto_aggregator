import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('crypto_aggregator')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


#celery -A config worker --beat --scheduler django_celery_beat.schedulers:DatabaseScheduler --loglevel=info
