import requests
from apps.exchanges.models import Exchange

OKX_NAME = "OKX"

def fetch_okx_info():
    url = "https://www.okx.com/api/v5/market/tickers?instType=SPOT"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            usdt_volume = sum(float(i['volCcy24h']) for i in data['data'] if 'USDT' in i['instId'])

            obj, created = Exchange.objects.update_or_create(
                slug='okx',
                defaults={
                    'name': OKX_NAME,
                    'logo_url': 'https://cryptologos.cc/logos/okex-logo.png',
                    'website': 'https://www.okx.com/',
                    'commission': 0.10,
                    'referral_link': 'https://www.okx.com/join',
                    'volume_24h': round(usdt_volume, 2),
                }
            )
            return obj
    except Exception as e:
        print("Error fetching OKX data:", e)
        return None