from abc import ABC, abstractmethod

class StateATM(ABC):

    @abstractmethod
    def insert_card(self, context):
        pass

    @abstractmethod
    def enter_pin_cod(self, context, pin):
        pass

    @abstractmethod
    def select_operation(self, context, operation):
        pass

    @abstractmethod
    def eject_card(self, context):
        pass


class NoCard(StateATM):

    def insert_card(self, context):
        print('Карта вставлена! Введите пин-код')
        context.state = HasCard()

    def enter_pin_cod(self, context, pin):
        print('Сначала вставьте карту!')

    def select_operation(self, context, operation):
        print('Сначала вставьте карту!')

    def eject_card(self, context):
        print('Карта не вставлена!')


class HasCard(StateATM):

    def insert_card(self, context):
        print('Карта уже вставлена! Введите пин-код')

    def enter_pin_cod(self, context, pin):
        if pin == 1234:
            print('Пин-код принят. Выберете операцию.')
            context.state = HasPin()
        else:
            print('Неверный пин-код')

    def select_operation(self, context, operation):
        print('Сначала введите пин-код')

    def eject_card(self, context):
        print('Карта извлечена!')
        context.state = NoCard()


class HasPin(StateATM):

    def insert_card(self, context):
        print('Карта уже вставлена! Выберете операцию')

    def enter_pin_cod(self, context, pin):
        print('Пин-код уже введен. Выберите операцию')

    def select_operation(self, context, operation):
        print(f'Вы выбрали операцию {operation}')
        context.state = NoCard()

    def eject_card(self, context):
        print('Карта извлечена')


class ATM:
    def __init__(self):
        self.state = NoCard()

    def insert_card(self):
        self.state.insert_card(self)

    def enter_pin(self, pin):
        self.state.enter_pin_cod(self, pin)

    def select_operation(self, operation):
        self.state.select_operation(self, operation)

    def eject_card(self):
        self.state.eject_card(self)

