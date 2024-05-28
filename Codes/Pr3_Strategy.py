class Strategy:
    def execute(self, a, b):
        pass

class Add(Strategy):
    def execute(self, a, b):
        return a + b

class Subtract(Strategy):
    def execute(self, a, b):
        return a - b

class Multiply(Strategy):
    def execute(self, a, b):
        return a * b

class Calculator:
    def __init__(self, strategy):
        self._strategy = strategy

    def execute_strategy(self, a, b):
        return self._strategy.execute(a, b)

# Пример использования
add_strategy = Add()
subtract_strategy = Subtract()
multiply_strategy = Multiply()

calculator = Calculator(add_strategy)
result = calculator.execute_strategy(5, 3)
print(result)  # Вывод: 8

calculator = Calculator(subtract_strategy)
result = calculator.execute_strategy(5, 3)
print(result)  # Вывод: 2

calculator = Calculator(multiply_strategy)
result = calculator.execute_strategy(5, 3)
print(result)  # Вывод: 15