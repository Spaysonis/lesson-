from tortoise import Tortoise
from model import User
from get_users import get_users_to_site


async def init_db():

    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['models']}
    )
    await Tortoise.generate_schemas()

async def populate_db():
    users = await get_users_to_site()

    for user in users:
        try:
            await User.create(
                id = user.get('id'),
                name = user.get('name'),
                email = user.get('email')
            )
            print(f"User {users.get('name')} added to DB.")
        except Exception as e:
            print(f'error {e}')


async def close_db():
    await Tortoise.close_connections()