class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def __get_rad(self):
        print("Get Radius")
        return self.__radius

    def __set_rad(self, radius):
        print("Set Radius")
        self.__radius = radius

    def __del_rad(self):
        print("Delete Radius")
        del self.__radius

    radius = property(fget=__get_rad, fset=__set_rad, fdel=__del_rad)


circle1 = Circle(30)
print(circle1.radius)
circle1.radius = 40

print(circle1.radius)
