class Burger:
    def __init__(self, size, cheese=False, pepperoni=False, lettuce=False, tomato=False):
        self.size = size
        self.cheese = cheese
        self.pepperoni = pepperoni
        self.lettuce = lettuce
        self.tomato = tomato

    def __str__(self):
        return f"Burger [size: {self.size}, cheese: {self.cheese}, pepperoni: {self.pepperoni}, lettuce: {self.lettuce}, tomato: {self.tomato}]"

class BurgerBuilder:
    def __init__(self, size):
        self.size = size
        self.cheese = False
        self.pepperoni = False
        self.lettuce = False
        self.tomato = False

    def add_cheese(self):
        self.cheese = True
        return self

    def add_pepperoni(self):
        self.pepperoni = True
        return self

    def add_lettuce(self):
        self.lettuce = True
        return self

    def add_tomato(self):
        self.tomato = True
        return self

    def build(self):
        return Burger(self.size, self.cheese, self.pepperoni, self.lettuce, self.tomato)

# Пример использования
builder = BurgerBuilder(2)
burger = builder.add_cheese().add_pepperoni().add_lettuce().build()
print(burger)