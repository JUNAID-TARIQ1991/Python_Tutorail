
from abc import ABC, abstractmethod
print(__name__)


class Shape(ABC):
    @abstractmethod
    def Area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def Area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def Area(self):
        return self.length * self.width


# def Area(shape):
 #   shape.Area()

# In the Area() function, you are calling shape.Area() without returning the result.
# As a result, when you call Area(rectangle) in the print()
# statement, the function returns None, which is why you're seeing "None" in the output.
def Area(shape):
    return shape.Area()


circle1 = Circle(2)
rectangle = Rectangle(12, 3)

print(isinstance(circle1, Shape))
print(Area(circle1))

print(Area(rectangle))
