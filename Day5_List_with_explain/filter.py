items = [('product1', 20), ('product2', 40), ('product3', 60)]
price = []
# # for a product whose price >30
# # method 1(old)
# for list in items:
#     if list[1] > 30:
#         price.append(list[1])
# print(price)

# method 2 (using lambda function)

x = list(filter(lambda item: item[1] >= 30, items))
print(x)


list1 = [['apple', 20], ['blueberry', 30], ['banana', 50], ['mango', 90]]
# use of lambda function only get the price of each
def x(item): return item


for i in x(list1):
    print(i[1])

# map function:
x = list(map(lambda item: item[1], list1))
print(x)

# filter function

x = list(filter(lambda item: item[1] >= 50, list1))
print(x)

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(filter(lambda x: (x % 2 != 0), li))
print(final_list)
