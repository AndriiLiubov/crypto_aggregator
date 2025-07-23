from .binance import fetch_binance_info
from .bybit import fetch_bybit_info
from .okx import fetch_okx_info

def fetch_all_exchanges():
    exchanges = []
    for fetcher in [fetch_binance_info, fetch_bybit_info, fetch_okx_info]:
        try:
            exchange = fetcher()
            if exchange:
                exchanges.append(exchange)
                print(f"✅ Обновлено: {exchange.name} — объем $ {exchange.volume_24h}")
            else:
                print("⚠️ Биржа не вернула данных.")
        except Exception as e:
            print(f"❌ Ошибка при обработке {fetcher.__name__}: {e}")
    return exchanges