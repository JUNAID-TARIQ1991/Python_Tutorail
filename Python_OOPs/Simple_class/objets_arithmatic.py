class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def get_zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"({self.x},{self.y})")

    def __str__(self):  # magic method
        return f"({self.x},{self.y})"

    def __add__(self, other):  # add magic method simply return a new object with new attributes(which are sum of attributes of two objects)
        return Point(self.x+other.x, self.y+other.y)


point0 = Point.get_zero()
point0.draw()
point1 = Point(3, 8)
point2 = Point(10, 5)

# with out __str__method you will get the memory address of this object (point1+pont2)
print(point1+point2)
# if __str__method is not defines we will create an other object.

add = point1+point2
print(add.x)

# compairing two objects:
