class Point:
    default_color = 'red'  # class level attribute
    # class level attributes shared among each object

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point: ({self.x},{self.y})")


point1 = Point(2, 7)
print(point1.default_color)
# when ever an object of Point class is created these atribute set to object by default
# we can define an attribute to object after the creation of object. Objects are dynamics in python i.e.
point1.z = 10
# The x , y and z attributes are called instance or object attributes. each object has unique set of attributes

point1.draw()

# another object
point2 = Point(3, 8)
print(point2.default_color)
point2.draw()

Point.default_color = "green"  # dynamic
print(point1.default_color)
