items = [('product1', 50), ('product2', 40), ('product3', 78)]

price = list(map(lambda item: item[1], items))
print(price)

items.sort(key=lambda items: items[1])

print(items)

price_filter = list(filter(lambda item: item[1] > 50, items))
print(price_filter)


# List comprehension

price = [item[1] for item in items]
print(price)

price_filter = [item for item in items if item[1] > 50]
print(price_filter)
