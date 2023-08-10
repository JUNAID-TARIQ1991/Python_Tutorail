class WriteCoordinateError(Exception):
    pass


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        raise WriteCoordinateError("X coordinate is read only")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        raise WriteCoordinateError("y coordinate is read only")


point = Point(2, 5)
print(point.x)
point.x = 5
