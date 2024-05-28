class Service:
    def __init__(self, name):
        self.name = name

    def execute(self):
        return f"Executing service {self.name}"


class ServiceConsumer:
    def __init__(self, service):
        self.service = service

    def consume_service(self):
        return self.service.execute()


service = Service("test_service")
service_consumer = ServiceConsumer(service)

print(service_consumer.consume_service())