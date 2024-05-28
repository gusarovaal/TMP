class Visitor:
    def visit(self, element):
        pass


class ElementA:
    def accept(self, visitor):
        visitor.visit(self)


class ElementB:
    def accept(self, visitor):
        visitor.visit(self)


class ConcreteVisitor(Visitor):
    def visit(self, element):
        if isinstance(element, ElementA):
            print("Visitor is visiting ElementA")
        elif isinstance(element, ElementB):
            print("Visitor is visiting ElementB")


# Пример использования
element_a = ElementA()
element_b = ElementB()

visitor = ConcreteVisitor()
element_a.accept(visitor)
element_b.accept(visitor)
