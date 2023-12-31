def show_double(number):  # number is the parameter
    double = number*2
    print(double)


def main():
    value = 5
    show_double(value)  # value is argument of the function show_double


main()


# function with multiple argument

def show_sum(num1, num2):
    sum = num1+num2
    print(sum)


def main():
    show_sum(12, 15)


main()

# A function can take string as an arguent


def reverse_name(name1, name2):   # Afunction simply take two parameters
    print(name2, name1)


def main():
    name1 = input("Enter your first_name:\t")
    print()
    name2 = input("Enter your secind name:\t")
    reverse_name(name1, name2)  # name1 and name 2 as argument of function


main()

# making changes to parameter


def change_me(val):
    val = 0
    print("The value of parameter is now ", val)


def main():
    value = input("Enter any number ")
    change_me(value)


main()

# in python you can pass valur to function by using keyword


def show_interest(principal, rate, periods):
    interest = principal * rate * periods
    print('The simple interest will be $',
          format(interest, ',.2f'),
          sep='')


def main():
    show_interest(principal=1000.0, rate=0.1, periods=10)


main()
