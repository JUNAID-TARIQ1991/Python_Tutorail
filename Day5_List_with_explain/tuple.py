point = (1, 3, 5, 7)
point1 = 1,
print(type(point1))

list = (1, 3) + (2, 4)  # we can concatinate tuple
print(list)

print(list * 4)

# we convert list to tuple:

list = [1, 4, 6, 7]
tup = tuple(list)

print(list)
print(tup)

string = "hello world"
tup2 = tuple(string)
print(tup2)
print(tup2[-1])  # like list we can access individual items of tuple

print(tup2[1: 3])  # 3 will no include

# we can unpack the tuple
tuple = (1, 3, 6)
x, y, z = tuple
print(x, y, z)


# swaping veriable
x = 5
y = 6
print(x, y)
z = x
x = y
y = z
print(x, y)

# Python program to demonstrate
# swapping of two variables

x = 10
y = 50

# Swapping of two variables
# Using third variable
temp = x
x = y
y = temp

print("Value of x:", x)
print("Value of y:", y)

# simple sweep code
x = 34
y = 87
print(x, y)
x, y = y, x  # here we are defining a tuple  and unpacking it x,y =(87,34)
a, b, c = 2, 4, 6

print(x, y)
