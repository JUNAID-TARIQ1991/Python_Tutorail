list = []
for x in range(5):
    list.append(x*2)

values = [x*2 for x in range(5)]  # this code is identical to the loop one
print(values)


# list comprehension not limited to list

list = {x*2 for x in range(5)}
print(list)

dict = {}
for x in range(5):
    dict[x] = x*3
print(dict)

for key, value in dict.items():
    print(key, value)

# how to add values in dicts usind dict comprehension

dict2 = {x: x*3 for x in range(1, 6)}
print(dict2)
