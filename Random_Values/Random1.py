import random
import string
print(random.random())  # random number b/w 0-1
print(random.randint(1, 7))
print(random.choice([1, 3, 4, 5, 7]))
# multiple values from this array
print(random.choices([1, 5, 6, 7, 8, 9], k=4))
print(random.choices("junaidtariq", k=4))

list = ["a", "e", "r"]
print("".join(list))  # join the strings and empty tring as seperator

print("".join(random.choices(string.ascii_letters+string.digits, k=7)))

# st = string
# print(st.ascii_letters)
array1 = [1, 3, 4, 5]
random.shuffle(array1)
print(array1)
