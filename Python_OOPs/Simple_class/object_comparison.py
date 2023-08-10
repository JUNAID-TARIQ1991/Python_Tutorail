class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def get_zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"({self.x},{self.y})")

    def __eq__(self, other):  # this is magic method, automatically calls when we insert == sign b/w objects
        # print(self.x == other.x and self.y == other.y)

        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y


point0 = Point.get_zero()
point0.draw()
point1 = Point(2, 5)
point2 = Point(2, 5)
point3 = Point(20, 40)
# compairing two objects:
print(point1 == point2)
print(point3 > point1)
