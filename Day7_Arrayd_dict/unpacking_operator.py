from pprint import pprint
import string
list1 = [x*2 for x in range(5)]
for x in list1:
    print(x)
number = [(5, 1), (1, 6), (3, 5)]


print("*********")
print(number)
print(*number)

value = list(range(5))
value1 = [*range(10), *"junaid"]
print(value1)

list2 = [2, 5, 9, 0]
list3 = [6, 7, 0, 3, 1]
list4 = [*list1, *list2]
print(list4)

# unpacking of dicts
dict1 = {"x": 3, "z": 4}
dict3 = {"y": 5, "t": 6}
# using unpacking operator we can combine the two list
dict5 = {**dict1, **dict3}
print(dict5)

# Exercise method1:
string1 = "This is common interview Question"
# alphabets = list(string.ascii_letters)
# print(alphabets)
# count = 0
# for char1 in string1.lower():
#     for char2 in string1.lower():
#         if char1 == char2:
#             count += 1
#     print(f"count of {char1}", count)
#     count = 0
# exercise method2
name = "junaid"

dict = {}


char_frequency = {}

for char in string1:

    if char in char_frequency:
        char_frequency[char] += 1

    else:
        char_frequency[char] = 1
pprint(char_frequency, width=1)
# this method will return key value pair in tuple
print(char_frequency.items())

# sorted function returned a list
x = (sorted(char_frequency.items(), key=lambda kv: kv[1], reverse=True))
print(x[0])
