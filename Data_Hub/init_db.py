

from Data_Hub.Model import User, Post
from Data_Hub.api import get_user_data, get_user_post
from tortoise import Tortoise

async def init_db():
    await Tortoise.init(
        db_url="sqlite://db.sqlite3",
        modules={'models': ['Data_Hub.Model']}
    )
    await Tortoise.generate_schemas()

    if not await User.all():
        print('База пуста, сейчас загружу! ')
        await populate_db_user()

    if not await Post.all():
        await populate_db_post()

async def populate_db_user():

    users_data = await get_user_data()

    for user in users_data:
        await User.create(
            id=user['id'],
            name=user['name'],
            email=user['email'],
            gender=user.get('gender', ''),
            status=user.get('status', '')
        )
async def populate_db_post():

    post_data = await get_user_post()

    for post in post_data:
        #user = await User.get(id=post['user_id'])
        await Post.create(
            id_post = post['id'],
            id_user = post['user_id'],
            title = post['title'],
            body = post['body']
        )






