import asyncio
import logging
import threading
import time
from abc import ABC, abstractmethod
from tortoise import Tortoise
logging.basicConfig(level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.CRITICAL)

class StateApi(ABC):
    """ИНИЦИАЛИЗАЦИЯ ТИПА МОЕНТЫ И ИНТЕРВАЛА ОБНОВЛЕНИЯ"""
    def __init__(self, currency, interval):
        self.currency = currency
        self.interval = interval


    @abstractmethod  # ПОЛУЧЕНИЕ ДАННЫХ С ЭНДПОИНТА
    def get_info_crypto(self):
        pass

    @abstractmethod  # ОБРАБОТКА ДАННЫХ ПОСЛЕ ПОЛУЧЕНИЯ
    def process_data(self, data):
        pass


    def start(self):  #  ЗАПУСК ФУНКЦИИ В МНОГОПОТОЧНОСТИ
        def run():
            try:
                while True:
                    data = self.get_info_crypto()
                    if data:
                        asyncio.run(self.process_data(data))
                    time.sleep(self.interval)
            except KeyboardInterrupt:
                logging.info('Программа остановлена вручную')
            finally:
                asyncio.run(Tortoise.close_connections())
                logging.info('База данных закрыта успешно!')
        thread = threading.Thread(target=run)
        thread.start()


