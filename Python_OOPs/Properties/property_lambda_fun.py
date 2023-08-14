
def x(a, b): return a * b  # x= lambda(a,b: a*b)


print(x(5, 6))


class Circle:
    def __init__(self, radius):
        self.__radius = radius
    radius = property(lambda self: self.__radius)


circle = Circle(40)
Circle.radius

print(Circle.radius.fget)
