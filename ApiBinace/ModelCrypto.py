from tortoise import Tortoise, fields
from tortoise.models import Model
import logging


class CryptoDB(Model):
    id = fields.IntField(pk=True)
    crypto_name = fields.CharField(max_length=50)
    price_crypto = fields.FloatField()



async def init():
    await Tortoise.init(
        db_url="sqlite://db.sqlite3",
        modules={"models": ["ApiBinace.ModelCrypto"]},
    )
    await Tortoise.generate_schemas(safe=True)
    logging.info('База данных инициализировалась успешно!')
    print("База данных инициализирована!")


# https://api.binance.com/api/v3/ticker/price


