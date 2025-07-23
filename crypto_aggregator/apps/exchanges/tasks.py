from celery import shared_task
from apps.exchanges.services.fetch_all import fetch_all_exchanges

@shared_task
def update_all_exchanges():
    fetch_all_exchanges()