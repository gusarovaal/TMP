from abc import ABC, abstractmethod


# Абстрактные классы для продуктов
class Button(ABC):
    @abstractmethod
    def draw(self):
        pass


class Checkbox(ABC):
    @abstractmethod
    def draw(self):
        pass


# Конкретные продукты
class WindowsButton(Button):
    def draw(self):
        print("Windows Button")


class MacButton(Button):
    def draw(self):
        print("Mac Button")


class WindowsCheckbox(Checkbox):
    def draw(self):
        print("Windows Checkbox")


class MacCheckbox(Checkbox):
    def draw(self):
        print("Mac Checkbox")


# Абстрактная фабрика
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass


# Конкретные фабрики
class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()


class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()


# Использование абстрактной фабрики
def create_gui(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()

    button.draw()
    checkbox.draw()


windows_factory = WindowsFactory()
mac_factory = MacFactory()

create_gui(windows_factory)
# Вывод: Windows Button
#        Windows Checkbox

create_gui(mac_factory)
# Вывод: Mac Button
#        Mac Checkbox
