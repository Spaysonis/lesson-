
from bs4 import BeautifulSoup
import httpx
import asyncio

async def get_info_crypto(params):

    url = 'https://api.binance.com/api/v3/ticker/price'

    async with httpx.AsyncClient() as client:
        try:
            responses = await client.get(url=url, params=params)
            if responses.status_code == 200:
                try:
                     return responses.json()
                except ValueError as e:
                    return f'error decoding json as {e}'
            else:
                return f'error {responses.status_code} - {responses.text}'
        except httpx.RequestError as e:
            return f'Request  error {e}'


async def get_crypto_price(symbol):
    param = {'symbol': symbol}
    res = await get_info_crypto(param)
    if res:
        print(f"Текущая цена {symbol}: {res['price']}")
    else:
        print(f"Не удалось получить данные для {symbol}")


async def main():
    await get_crypto_price('BTCUSDT')
    await get_crypto_price('SOLUSDT')


if __name__ == "__main__":
    asyncio.run(main())

