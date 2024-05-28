class Component:
    def __init__(self, name):
        self.name = name

    def operation(self):
        pass


class Leaf(Component):
    def operation(self):
        print(f"Leaf is performing operation")


class Composite(Component):
    def __init__(self, name):
        super().__init__(name)
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def operation(self):
        print(f"Composite is performing operation")
        for child in self.children:
            child.operation()

# Usage
leaf1 = Leaf("Leaf 1")
leaf2 = Leaf("Leaf 2")
leaf3 = Leaf("Leaf 3")

composite = Composite("Composite 1")
composite.add_child(leaf1)
composite.add_child(leaf2)

composite2 = Composite("Composite 2")
composite2.add_child(leaf3)
composite2.add_child(composite)

composite2.operation()
