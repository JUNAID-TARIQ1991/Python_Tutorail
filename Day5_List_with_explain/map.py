items = [('product1', 30), ('product2', 40), ('product3', 60)]

price = []
for item in items:
    price.append(item[1])
print("Price List", price)

# lambda function


def x(item): return item


for item in x(items):
    print(item[1])


# print(x(items))
# map function:
x = map(lambda item: item[1], items)

for i in x:
    print(i)


x = list(map(lambda item: item[1], items))
print(x)
