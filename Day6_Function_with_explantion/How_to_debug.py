# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total


# print(multiply(1, 4, 6))


def fizz_buzz(number):
    if number % 3 == 0 and number / 3 == 1:
        print("Fizz")
    elif number % 5 == 0 and number / 5 == 1:
        print("Buzz")
    elif number % 3 == 0 and number % 5 == 0:
        print("Fizz_buzz")
    else:
        print(number)


fizz_buzz(23)
