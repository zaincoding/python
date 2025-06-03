
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
class Rectangel(Shape):
    def __init__(self, width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
obj1 = Rectangel(5,5)

print(obj1.area())