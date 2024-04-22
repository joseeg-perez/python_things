from abc import ABC, abstractmethod

class AbstractClassExample(ABC):
    def __init__(self, value) -> None:
        super().__init__()
        self.value = value

    @abstractmethod
    def do_something(self):
        pass