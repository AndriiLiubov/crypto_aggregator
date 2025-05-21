from celery import shared_task
from apps.coins.utils.coinmarketcap import fetch_and_update_coin_data

@shared_task
def update_coin_data_task():
    fetch_and_update_coin_data()
