from abc import ABC, abstractmethod
import threading
import time
import httpx
from yarl import URL


class ApiCrypto(ABC):

    def __init__(self, currency, period):
        self.currency = currency
        self.period = period

    @abstractmethod
    def get_currency(self):
        pass

    @abstractmethod
    def display_currency(self, data):
        pass

    def start(self):
        def run():
            while True:
                data = self.get_currency()
                if data:
                    self.display_currency(data)
                    time.sleep(self.period)
        thread = threading.Thread(target=run)
        thread.start()

class CryptoPair(ApiCrypto):

    def get_currency(self):
        url = URL('https://api.binance.com/api/v3/ticker/price').with_query(symbol=self.currency)
        #params = {'symbol': self.currency}

        response = httpx.get(url=str(url))
        if response.status_code == 200:
            return response.json()

    def display_currency(self, data):
        print(f"=== {self.currency} ===")
        print(f"Symbol: {data['symbol']}")
        print(f"Price: {data['price']}")
        print("=" * 20)


btc = CryptoPair(currency='BTCUSDT', period=2)
sol = CryptoPair(currency='SOLUSDT', period=4)
btc.start()
sol.start()