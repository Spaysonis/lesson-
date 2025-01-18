
from fastapi import FastAPI
from Data_Hub.init_db import init_db
from tortoise import Tortoise
from contextlib import asynccontextmanager
from Data_Hub.Model import User, Post


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Инициализация базы данных...")
    await init_db()  # Инициализация базы данных
    print("Инициализация базы данных успешна!")
    yield
    await Tortoise.close_connections()
    print("Connections closed.")
app = FastAPI(lifespan=lifespan)




@app.get('/')
async def start():
    return f'Добро пожаловать!'


@app.get('/users')
async def get_user():
    user = await User.all()
    return user

@app.get('/users/{user_id}')
async def get_user_by_id(user_id: int):
    user = await User.get(id=user_id)
    return user

@app.get('/users/{user_id}/post')
async def get_user_messages(user_id: int):
    try:
        messages = await Post.filter(id_user=user_id)
        if not messages:
            return {'error': 'Сообщения не найдены для данного пользователя'}
        return messages
    except Exception as e:
        return {'error': str(e)}




if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
