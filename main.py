import uvicorn
from fastapi import FastAPI
from Data_Hub.Model import User
from Data_Hub.init_db import init_db
from tortoise import Tortoise

app = FastAPI()

# Хендлер для получения списка всех пользователей
@app.get("/users")
async def get_users():
    users = await User.all()
    return users