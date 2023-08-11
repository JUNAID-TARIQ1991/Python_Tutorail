from Rectangle_cube import Rectangle


class Cube(Rectangle):

    def __init__(self, height, length, width):
        self.__height = height
        super().__init__(length, width)
    """You define the Cube class, which inherits from the Rectangle class. 
    In the constructor (__init__), you initialize the __height attribute specific to the cube. 
    You pass length and width directly to parent class constructor."""

    def volume(self):
        return self.__height * self.Area
    """This method calculates and returns the volume of the cube by multiplying the cube's
    height with the inherited Area property from the parent Rectangle class."""


cube1 = Cube(12, 12, 3)
print(cube1.volume())
rectangle = Rectangle(13, 14)
print(rectangle.Area)
print(rectangle.length)
"""You create an instance of the Rectangle class with a length of 13 and a width of 14. 
You then access the Area property of the rectangle instance as an attribute and assign 
it to the area_value variable. Finally, you print the calculated area value."""
