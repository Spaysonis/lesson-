

class Pizza:

    def __init__(self, type_pizza:str, ingredient:list[str]):
        self.type_pizza = type_pizza
        self.ingredient = ingredient


    def info_pizza(self):
        return f'Пицца: {self.type_pizza}, Ингредиенты: {", ".join(self.ingredient)}'



class FactoryPizza:

    pizza_recipes = {
        'Mozzarella':['Tomate', 'Cheese', 'Olives'],
        'Vegan':['Tomate', 'Olives', 'Parsley']
    }

    def create_pizza(self, pizza_type):
        ingredient = self.pizza_recipes.get(pizza_type)
        if ingredient:
            return Pizza(pizza_type, ingredient)
        else:
            raise ValueError(f"Unknown pizza type: {pizza_type}")

try:
    factory = FactoryPizza()
    pizza = factory.create_pizza('Vegan')
    pizza1 = factory.create_pizza('Mozzarella')
    print(pizza1.info_pizza())
    print(pizza.info_pizza())


except ValueError as e:
    print(f'error {e}')








