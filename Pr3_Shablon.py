from abc import ABC, abstractmethod


class AlgorithmTemplate(ABC):

    @abstractmethod
    def step1(self):
        pass

    @abstractmethod
    def step2(self):
        pass

    @abstractmethod
    def step3(self):
        pass

    def run_algorithm(self):
        self.step1()
        self.step2()
        self.step3()


class ConcreteAlgorithm1(AlgorithmTemplate):

    def step1(self):
        print("Step 1 for Concrete Algorithm 1")

    def step2(self):
        print("Step 2 for Concrete Algorithm 1")

    def step3(self):
        print("Step 3 for Concrete Algorithm 1")


class ConcreteAlgorithm2(AlgorithmTemplate):

    def step1(self):
        print("Step 1 for Concrete Algorithm 2")

    def step2(self):
        print("Step 2 for Concrete Algorithm 2")

    def step3(self):
        print("Step 3 for Concrete Algorithm 2")


if __name__ == "__main__":
    algorithm1 = ConcreteAlgorithm1()
    algorithm1.run_algorithm()

    algorithm2 = ConcreteAlgorithm2()
    algorithm2.run_algorithm()