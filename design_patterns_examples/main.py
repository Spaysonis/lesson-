from  ATM import ATM
from BrightMethodTVControl import RemoveControl, Tv
from FactoryMethodPizza import FactoryPizza, Pizza
from StateMethodCoffeeMachine import CoffeeMachine


def main():

    # Экземпляр класса банкомата
    atm = ATM()

    # Экземпляр класса тв и пульт
    tv = Tv()
    rem_control = RemoveControl(tv)

    # Экземпляр класса Пиццерии
    factory_pizza = FactoryPizza()

    # Экземпляр класса кофе машины
    coffee_machine = CoffeeMachine()


    """ATM"""
    atm.insert_card() # Вставлю карту в банкомат
    atm.enter_pin(1234) # Ввожу пин код
    atm.select_operation('Снять деньги') # Выбираю операцию
    atm.eject_card() # Забираю карту
    print('------------------')

    """TV AND CONTROLLER"""
    tv.turn_on() # Включаю телевизор
    tv.set_chanel(12) # Выбираю канал
    tv.turn_off() # Выключаю телевизор
    print('------------------')

    """PIZZA FACTORY"""
    mozzarella = factory_pizza.create_pizza('Vegan')  # Заказываю пиццу
    mozzarella.info_pizza()  # Получаю информацию о пицце
    print('------------------')

    """COFFEE MACHINE"""
    coffee_machine.check_status() # перевожу кофе машину в режим ожидания
    coffee_machine.start()  # готовлю кофе
    coffee_machine.off()  #  выключаю кофе



if __name__  == '__main__':
    main()








