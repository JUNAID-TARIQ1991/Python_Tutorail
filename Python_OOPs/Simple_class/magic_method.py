class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):  # magic method
        return f"({self.x},{self.y})"

    @classmethod  # decorator
    def Zero(cls):  # in instance method self is reference to object, here cls is reference to Class
        # when we call this method, object automatically refered to this method using self parameter
        return cls(0, 0)

    def draw(self):
        print(f"Point: ({self.x},{self.y})")


# class method
point0 = Point.Zero()  # here this point class automatically efered to zero method
point0.draw()
point1 = Point(2, 7)
point2 = Point(3, 8)
print(point1.draw())
print(point1)
print(str(point1))
