from abc import ABC, abstractmethod


class StateTv(ABC):

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def set_chanel(self, chanel:int):
        pass


class Tv(StateTv):

    def turn_on(self):
        print('Телевизор включен')

    def turn_off(self):
        print('Телевизор выключен')

    def set_chanel(self, chanel: int):
        print(f'Телевизор переключен на {chanel} канал')

class RemoveControl:

    def __init__(self, device):
        self.device = device

    def turn_on(self):
        self.device.turn_on()

    def turn_off(self):
        self.device.turn_off()

    def set_chanel(self, chanel):
        self.device.set_chanel(chanel)


lg = Tv()

remove_tv = RemoveControl(lg)


remove_tv.turn_on()
remove_tv.set_chanel(12)
remove_tv.turn_off()

