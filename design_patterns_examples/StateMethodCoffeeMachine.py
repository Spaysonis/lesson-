from abc import ABC, abstractmethod

class StateMachine(ABC):

    @abstractmethod
    def off_machine(self, context):
        pass

    @abstractmethod
    def enter_waiting_mod(self, context):
        pass

    @abstractmethod
    def create_coffee(self, context):
        pass

    @abstractmethod
    def finish_coffe(self, context):
        pass


class StartMachine(StateMachine):

    def off_machine(self, context):
        print('Машина выключена!!')
        context.state = Stop()

    def enter_waiting_mod(self, context):
        print('Перехожу в режим ожидания!!')
        context.state = Waiting()

    def create_coffee(self, context):
        print('Машина выключена!! Перейдите в режим ожидания!!')

    def finish_coffe(self, context):
        print('Ошибка!! Машина выключена!!')

class Waiting(StateMachine):

    def off_machine(self, context):
        print('Выключаю машину!!! До свидания!')
        context.state = Stop()

    def enter_waiting_mod(self, context):
        print('Перехожу к приготовлению напитка!!!!')
        context.state = CreateCoffee()

    def create_coffee(self, context):
        print('Приготовление кофе!! Подождите!!')

    def finish_coffe(self, context):
        print('Ошибка!! Кофе еще не готов!!')

class CreateCoffee(StateMachine):

    def off_machine(self, context):
        print('Выключаю машину!!! До свидания!')
        context.state = Stop()

    def enter_waiting_mod(self, context):
        print('Ваш напиток почти готов! Перехожу в режим ожидания!')
        context.state = Waiting()

    def create_coffee(self, context):
        print('Дождитесь приготовления напитка!!!')

    def finish_coffe(self, context):
        print('Ваш напиток готов!! Возвращаюсь в режим ожидания!')
        context.state = Waiting()

class Stop(StateMachine):

    def off_machine(self, context):
        print('Машина уже выключена!! ')

    def enter_waiting_mod(self, context):
        print('Перехожу в режим ожидания!! ')
        context.state = Waiting()

    def create_coffee(self, context):
        print('Машина выключена! Перейдите в режим ожидания!!')

    def finish_coffe(self, context):
        print('Ошибка!! Машина выключена!!')


class CoffeeMachine:

    def __init__(self):
        self.state = Stop()

    def start(self):
        self.state.enter_waiting_mod(self)

    def check_status(self):
        self.state.enter_waiting_mod(self)

    def off(self):
        self.state.off_machine(self)


