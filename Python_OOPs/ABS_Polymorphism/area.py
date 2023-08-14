from abc import ABC, abstractmethod
import ABC_example


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height


# Create instances of different shapes
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)

# Calculate and print the areas
shapes = [circle, rectangle, triangle]
for shape in shapes:
    print(f"Area of {shape.__class__.__name__}: {shape.calculate_area()}")


square = ABC_example.Square()
square.sides()
