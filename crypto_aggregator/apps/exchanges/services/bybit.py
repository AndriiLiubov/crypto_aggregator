import requests
from apps.exchanges.models import Exchange

BYBIT_NAME = "Bybit"


def fetch_bybit_info():
    url = "https://api.bybit.com/v5/market/tickers?category=spot"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            tickers = data.get("result", {}).get("list", [])
            usdt_volume = sum(
                float(i.get("quoteVolume24h", 0))
                for i in tickers if "USDT" in i.get("symbol", "")
            )

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

