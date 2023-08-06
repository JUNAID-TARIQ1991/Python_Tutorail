from sys import getsizeof
list = (x*2 for x in range(100000))

print(getsizeof(list))
# generator objects are very use ful when we are dealing with large data sets.
