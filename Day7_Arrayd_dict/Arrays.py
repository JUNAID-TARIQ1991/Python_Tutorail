# onlu useful when dealing with large et of values
# unlike list arrays only support single data type
# i.e. array of integer, array of string, array of float
from array import array
number = array('i', [1, 4, 6, 8, 9, 4, 3, 67, 66])
print(number)
number.append(4)
print(number)


# Set are also useful datatype in python

list = [1, 3, 4, 4, 5, 5, 6, 6, 8, 5, 3]
set1 = {1, 4, 6, 8}
set2 = {1, 5, 7, 8, 9, 23}

print(set1 | set2)  # union
print(set1 & set2)  # intersection
print(set1 - set2)  # difference
print(set1 ^ set2)
