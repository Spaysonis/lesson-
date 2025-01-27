

class Pizza:

    def __init__(self, type_pizza:str, ingredient:list[str]):
        self.type_pizza = type_pizza
        self.ingredient = ingredient


    def info_pizza(self):
        print( f'Пицца: {self.type_pizza}, Ингредиенты: {", ".join(self.ingredient)}')



class FactoryPizza:

    pizza_recipes = {
        'Mozzarella':['Tomate', 'Cheese', 'Olives'],
        'Vegan':['Tomate', 'Olives', 'Parsley']
    }

    def create_pizza(self, pizza_type):
        ingredient = self.pizza_recipes.get(pizza_type)
        if ingredient:
            print(f'заказ на {pizza_type} сформирован')
            return Pizza(pizza_type, ingredient)
        else:
            raise ValueError(f"Unknown pizza type: {pizza_type}")









