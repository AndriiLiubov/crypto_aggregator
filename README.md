which python3

if not /Users/andrii/VScode_projects/crypto_aggregator/.venv/bin/python3

source .venv/bin/activate

cd crypto_aggregator

run postgres and redis in docker

python manage.py runserver

celery -A config worker --beat --scheduler django_celery_beat.schedulers:DatabaseScheduler --loglevel=info