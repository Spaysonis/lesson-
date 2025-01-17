import asyncio

import httpx
from httpx import AsyncClient
from settings import API_URL, TOKEN


async def get_users_to_site():

    headers = {
        "Authorization": f"Bearer {TOKEN}"
    }

    async with AsyncClient() as client:
        response = await client.get(API_URL, headers=headers)
        if response.status_code == 200:
            return response.json()




