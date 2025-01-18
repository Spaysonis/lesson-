from tortoise import Model
from tortoise import fields


class User(Model):
    """Модель класс user"""
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    email = fields.CharField(max_length=100)
    gender = fields.CharField(max_length=50)
    status = fields.CharField(max_length=50)

    class Meta:
        table_name = 'user'


class Post(Model):
    """Модель класса постов"""
    id_post = fields.IntField(pk=True)
    id_user =  fields.IntField()
    title = fields.CharField(max_length=100)
    body = fields.TextField()

    class Meta:
        table_name = 'post'

