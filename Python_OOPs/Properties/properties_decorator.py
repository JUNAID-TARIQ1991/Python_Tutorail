# this program wil run fine and in the constructor our set_Price function kicks in.
# but there is a better way to write this program
# using buit in python functon called property


# In the given code, the Products class is defined in a more concise way, using the @property decorator and
# its corresponding setter. The @property decorator is a built-in Python feature that allows
# you to define a method as a read-only property of a class. The corresponding setter decorator
# @price.setter enables you to define a method as a property setter, which handles attribute modification.
class Products:
    def __init__(self, price):
        self.price = price
# The @property decorator is used to define the price method as a read-only property.
# This means that you can access the price method as if it were an attribute,
# without explicitly calling it like a method. The property method price returns the value of the
# private attribute __price.

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price can't be negative")
        else:
            self.__price = value

    # price = property(get_Price, set_Price)
car = Products(500)
print(car.price)
Cycle = Products(50)
print(Cycle.price)
Cycle.price = 30
print(Cycle.price)
Cycle.price = 0
