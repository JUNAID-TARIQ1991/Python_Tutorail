# this program wil run fine and in the constructor our set_Price function kicks in.
# but there is a better way to write this program
# using buit in python functon called property
class Products:
    def __init__(self, price):
        self.set_Price(price)

    def get_Price(self):
        return self.__price

    def set_Price(self, value):
        if value < 0:
            raise ValueError("Price can't be negative")
        else:
            self.__price = value
    price = property(get_Price, set_Price)


product = Products(660)
print(product.price)
product.price = 20
print(product.price)


product2 = Products(500)
print(product2.price)
# product.price = 300
# print(product.get_Price())
# product.set_Price(556)
# print(product.get_Price())

# this program wil run fine and in the constructor our set_Price function kicks in.
# but there is a better way to write this program
# using buit in python functon called property

# Explanation:
"""In the given code, a class named Products is defined, and it represents a product 
with a price attribute. The class has a getter method get_Price() and a setter method set_Price(value) 
to get and set the price of the product, respectively. The class also uses the property built-in Python 
function to simplify the process of setting and getting the price attribute.

Here's a breakdown of the code:

Class Definition:

python
Copy code
class Products:
Constructor (__init__ method):
The constructor is called when you create an instance of the Products class. 
It takes a price parameter, and it sets the price using the set_Price method.

python
Copy code
def __init__(self, price):
    self.set_Price(price)
Getter method (get_Price):
The get_Price method is used to retrieve the value of the __price attribute (the actual 
price of the product).

python
Copy code
def get_Price(self):
    return self.__price
Setter method (set_Price):
The set_Price method is used to set the value of the __price attribute. It checks 
if the provided value is non-negative (greater than or equal to 0). If the value is negative, 
it raises a ValueError with a custom error message.

python
Copy code
def set_Price(self, value):
    if value < 0:
        raise ValueError("Price can't be negative")
    else:
        self.__price = value
Property function:
The property built-in Python function is used to create a property object for 
the price attribute. It takes two arguments: the getter function (get_Price) and the setter 
function (set_Price). The property function allows you to access the methods like attributes.

The line price = property(get_Price, set_Price) creates a property 
named price that uses the get_Price method to retrieve the value and the set_Price method to set 
the value.

Creating Instances of the Class and Using the Property:
The code then creates two instances of the Products class (product and product2) with different 
prices and demonstrates how to access and modify the price attribute using the property.

For example, when you run the code, it will output:

Copy code
660
20
500
The first product's price is set to 660 initially, and then it is updated to 20 using the property. The second product's price is set to 500 during initialization.

By using the property function, the code achieves a more elegant and Pythonic way of 
handling attribute access and modification. Instead of explicitly calling the getter and setter methods, you can use the price property as if it were a regular attribute. This simplifies the syntax and makes the code more readable. Additionally, you can add custom validation or additional 
logic to the getter and setter methods as needed.
"""
