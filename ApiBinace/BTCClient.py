import asyncio
import logging
import httpx
from ApiBinace.AbstractApi import StateApi
from ApiBinace.ModelCrypto import init, CryptoDB
import time


class BitcoinClient(StateApi):

    def __init__(self, currency, interval):
        super().__init__(currency, interval)
        asyncio.run(init())
        self.save_to_db = CryptoDB()


    def get_info_crypto(self):

        url = 'https://api.binance.com/api/v3/ticker/price'
        param = {'symbol':self.currency}

        response = httpx.get(url=url, params=param)
        try:
            if response.status_code == 200:
                return response.json()

            else:
                logging.info(f'status code {response.status_code}')
        except httpx.RequestError as e:
            logging.info(f'error httpx {e}')


    async def process_data(self, data):

        name_currency = data['symbol']
        price_currency = data['price']

        if name_currency == 'BTCUSDT':
            record = await self.save_to_db.create(crypto_name=name_currency, price_crypto=price_currency)
            if record:
                current_time = time.localtime()
                formatted_time = time.strftime("%H:%M:%S", current_time)
                logging.info(formatted_time)


