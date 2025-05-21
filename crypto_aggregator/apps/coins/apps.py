from django.apps import AppConfig


class CoinsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.coins'

"""
    def ready(self):
        from .utils.coinmarketcap import fetch_and_update_coin_data
        fetch_and_update_coin_data()
""" 