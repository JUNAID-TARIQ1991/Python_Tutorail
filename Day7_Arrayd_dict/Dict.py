set1 = {1, 1, 4, 6, 3, 6}

set1 = {"x": 1, "y": 2}
print(set1["x"])
# these are called dictionaries
# list
# tuple
# set
# dict
dict1 = dict(junaid="EHEP", Zohaib="Accounts", Qudsia="Teacher")
print(dict1["Zohaib"])

print(dict1.get("junaid"))  # this will return value associated with this key
# this will return value associated with this key
print(dict1.get("junaid", 0))  # if not found return 0

# similarly to delete we use del key word with key of that value


print(dict1)
# how to access dict element:
for key in dict1:
    print(key, dict1[key])
# another method:
for x in dict1.items():
    print(x)

for key, value in dict1.items():
    print(key, value)
