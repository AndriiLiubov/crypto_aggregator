import requests
from apps.exchanges.models import Exchange

BINANCE_NAME = "Binance"


def fetch_binance_info():
    url = "https://api.binance.com/api/v3/ticker/24hr"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            # Допустим, возьмем USDT объем как обобщенный объем биржи
            usdt_volume = sum(float(i['quoteVolume']) for i in data if 'USDT' in i['symbol'])

            obj, created = Exchange.objects.update_or_create(
                slug='binance',
                defaults={
                    'name': BINANCE_NAME,
                    'logo_url': 'https://cryptologos.cc/logos/binance-coin-bnb-logo.png',
                    'website': 'https://www.binance.com/',
                    'commission': 0.10,
                    'referral_link': 'https://www.binance.com/en/activity/referral-entry',
                    'volume_24h': round(usdt_volume, 2),
                }
            )
            return obj
    except Exception as e:
        print("Error fetching Binance data:", e)
        return None