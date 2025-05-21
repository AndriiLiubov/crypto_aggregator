import requests
from datetime import datetime
from ..models import Coin

API_KEY = 'b2ee40ff-47f0-48db-894b-0758c301b5d5'
URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

HEADERS = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': API_KEY,
}

def fetch_and_update_coin_data():
    response = requests.get(URL, headers=HEADERS, params={'limit': 20, 'convert': 'USD'})
    data = response.json()

    for item in data['data']:
        Coin.objects.update_or_create(
            symbol=item['symbol'],
            defaults={
                'name': item['name'],
                'price': item['quote']['USD']['price'],
                'market_cap': item['quote']['USD']['market_cap'],
                'volume_24h': item['quote']['USD']['volume_24h'],
                'percent_change_24h': item['quote']['USD']['percent_change_24h'],
                'last_updated': datetime.strptime(item['last_updated'], "%Y-%m-%dT%H:%M:%S.%fZ"),
            }
        )
