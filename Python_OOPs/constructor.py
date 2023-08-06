class Point:

    def __init__(self, x, y, z):
        print("this is constructor")
        self.x = x
        self.y = y
        self.z = z

    def draw(self):
        print(f"points ({self.x},{self.y},{self.z})")


point2 = Point(1, 4, 6)
print(point2.x)
point2.draw()
