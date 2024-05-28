from abc import ABC, abstractmethod

# Абстрактный класс Subject
class Subject(ABC):
    @abstractmethod
    def request(self) -> None:
        pass

# Реальный класс RealSubject
class RealSubject(Subject):
    def request(self) -> None:
        print("RealSubject: Processing request")

# Класс Proxy
class Proxy(Subject):
    def __init__(self) -> None:
        self._real_subject = RealSubject()

    def request(self) -> None:
        if self.check_access():
            self._real_subject.request()
        else:
            print("Proxy: Access denied")

    def check_access(self) -> bool:
        # Проверка доступа пользователя
        return True

# Клиентский код
def client_code(subject: Subject) -> None:
    subject.request()

# Тестирование
real_subject = RealSubject()
client_code(real_subject)

proxy = Proxy()
client_code(proxy)