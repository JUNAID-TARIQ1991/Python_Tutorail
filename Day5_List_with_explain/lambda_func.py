# lambda function
def lambda_cube(y): return y*y


print(lambda_cube(5))

is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]

# iterate on each lambda function
# and invoke the function to get the calculated value
for item in is_even_list:
    print(item())
# lambda function with if:else

# Max =lambda a, b : a if a>b else b


def Max(a, b): return a if (a > b) else b


print(Max(4, 1))


list = [[3, 7], [1, 2], [3, 4], [6, 8]]
def sort_list(x): return (sorted(i) for i in x)


for i in sort_list(list):
    print(i)


# print(sorted(number))

# print(sorted(number, reverse=True))
# number.sort(reverse=True)

# print(number)
# number.sort()
# print(number)


# But how to sort list with multiple data types or with tuples.
list = [(1, 2), (2, 3), (4, 6)]


def ret_list(tup):
    return tup[0]


# 33333
list = [
    ("product1", 30),
    ("product2", 20),
    ("product3", 50)

]


list.sort(key=lambda item: item[1])
print(list)


def sort_item(item):
    return item[1]


list.sort(key=sort_item)
# print(list)


def double(x): return x*x


print(double(5))
