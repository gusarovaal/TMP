class Mediator:
    def __init__(self):
        self.colleague1 = Colleague1(self)
        self.colleague2 = Colleague2(self)

    def notify(self, sender, event):
        if sender == self.colleague1:
            print(f'Colleague1 triggered event: {event}')
        elif sender == self.colleague2:
            print(f'Colleague2 triggered event: {event}')

class Colleague1:
    def __init__(self, mediator):
        self.mediator = mediator

    def do_something(self):
        self.mediator.notify(self, 'do_something')

class Colleague2:
    def __init__(self, mediator):
        self.mediator = mediator

    def do_something_else(self):
        self.mediator.notify(self, 'do_something_else')

if __name__ == '__main__':
    mediator = Mediator()
    mediator.colleague1.do_something()
    mediator.colleague2.do_something_else()
