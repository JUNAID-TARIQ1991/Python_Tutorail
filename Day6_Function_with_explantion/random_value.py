import random


def main():
    print("We are going to toss a coin 10 times")
    for count in range(0, 10):
        x = random.randint(1, 2)  # randint return integer
        if x == 1:
            print("Head")
        else:
            print("Tail")


main()

number = random.randrange(1, 10)  # randrange also return integer
print(number)
number = random.randrange(0, 100, 10)
print(number)

number = random.random()
print(number)

# Yes, that's correct. In Python, the random.random() function returns a
# floating-point number in the range [0.0, 1.0).
# It generates a random float value greater than or equal to 0.0 and less than 1.0.

number = random.uniform(1, 10)
print(number)
