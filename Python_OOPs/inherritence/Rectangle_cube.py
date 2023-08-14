
if __name__ == "__min__":

    class Rectangle:
        def __init__(self, length, width):
            self.__Rlength = length
            self.__Rwidth = width

        @property
        def length(self):
            return self.__Rlength

        @length.setter
        def length(self, length):
            self.__Rlength = length

        @property
        def width(self):
            return self.__Rwidth

        @width.setter
        def width(self, width):
            self.__Rwidth = width

        @property
        def Area(self):
            return self.__Rwidth * self.__Rlength


"""In this section, you define the Rectangle class with private attributes __Rlength and __Rwidth 
to encapsulate the length and width of the rectangle. Properties are defined for length, width, and Area. 
The @property decorator allows you to access these methods like attributes."""
