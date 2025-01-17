from tortoise import Model
from tortoise import fields

class User(Model):

    __column_name__= 'user'

    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    email = fields.CharField(max_length=100)

    def __str__(self):
        return f'{self.id}:{self.name} - {self.email}'
