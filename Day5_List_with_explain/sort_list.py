number = [1, 4, 6, 34, 76, 45, 2, 1, 0]
number.append(3)
print(number.count(1))
print(number.pop(0))
print(number)
# print(sorted(number))

# print(sorted(number, reverse=True))
# number.sort(reverse=True)

# print(number)
# number.sort()
# print(number)

# But how to sort list with multiple data types or with tuples.

list = [
    ("product1", 30),
    ("product2", 20),
    ("product3", 50)

]


def sort_item(item):
    return item[1]


list.sort(key=sort_item)
print(list)
