import requests
from apps.exchanges.models import Exchange

BYBIT_NAME = "Bybit"

def fetch_bybit_info():
    url = "https://api.bybit.com/v2/public/tickers"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            usdt_volume = sum(float(i['quote_volume_24h']) for i in data['result'] if 'USDT' in i['symbol'])

            obj, created = Exchange.objects.update_or_create(
                slug='bybit',
                defaults={
                    'name': BYBIT_NAME,
                    'logo_url': 'https://cryptologos.cc/logos/bybit-logo.png',
                    'website': 'https://www.bybit.com/',
                    'commission': 0.10,
                    'referral_link': 'https://www.bybit.com/invite',
                    'volume_24h': round(usdt_volume, 2),
                }
            )
            return obj
    except Exception as e:
        print("Error fetching Bybit data:", e)
        return None
