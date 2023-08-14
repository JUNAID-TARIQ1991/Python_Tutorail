# Properties with decorator

class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
# length property

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, width):
        self.__length = length

    @length.deleter
    def __deletelen(self):
        del self.__length

 # width property

    def __get_wid(self):
        return self.__width

    def __setwid(self, width):
        self.__width = width

    def __deletewid(self):
        del self.__width
    width = property(__get_wid, __setwid, __deletewid)


square = Rectangle(12, 12)
print(square.length)
print(square.width)

square.width = 16
print(square.width)

del square.width
square.width
