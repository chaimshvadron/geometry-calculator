from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__} with area: {self.get_area()}"
