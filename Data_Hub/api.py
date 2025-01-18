import httpx
from Data_Hub.seting import API_URL_USER, API_URL_POST ,TOKEN


async def get_data_from_api(url:str):
    """ФУНКЦИЯ ДЛЯ ПОЛУЧЕНИЯ ДАННЫХ С САЙТА ПО URL"""

    headers = {"Authorization": f"Bearer {TOKEN}"} # Token site

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers)
            if response.status_code == 200:
                try:
                    return response.json()
                except ValueError as e:
                    return f'error decoding json as {e}'
            else:
                return f'error {response.status_code} - {response.text}'
        except httpx.RequestError as e:
            return f'Request  error {e}'



async def get_user_data():
    """ ФУНКЦИЯ ДЛЯ ПОЛУЧЕНИЯ ДАННЫХ О USERS"""
    return await get_data_from_api(API_URL_USER)

async def get_user_post():
    """ ФУНКЦИЯ ДЛЯ ПОЛУЧЕНИЯ ДАННЫХ POST - USERS"""
    return await get_data_from_api(API_URL_POST)














