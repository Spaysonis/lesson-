

class WashingMachine:

    def __init__(self, power=False, name_mode=None):
        self.power = power
        self.name_mode = name_mode

    def power_on(self, state:bool):
        self.power = state
        return f'Стиральная машина ' + ('ON' if state else 'OFF')

    def select_mode(self, mode:str):
        if not self.power:
            return 'Машина выключена!'
        self.name_mode = mode
        return f'Выбран режим {self.name_mode}'




