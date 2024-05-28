# Target interface
class Target:
    def request(self) -> str:
        pass

# Adaptee class to be adapted
class Adaptee:
    def specific_request(self) -> str:
        return "Adaptee's specific request"

# Adapter class implementing the Target interface
class Adapter(Target):
    def __init__(self, adaptee: Adaptee):
        self.adaptee = adaptee

    def request(self) -> str:
        return f"Adapter: {self.adaptee.specific_request()}"

# Client code
def client_code(target: Target) -> None:
    print(target.request())

# Usage example
adaptee = Adaptee()
adapter = Adapter(adaptee)

client_code(adapter)  # Output: Adapter: Adaptee's specific request
