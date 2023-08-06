try:

    age = int(input("Enter your age:"))
    xfact = 10/age
except ValueError as ex:
    print("You did't enter a valid age")
    print(type(ex))
except ZeroDivisionError:
    print("Can't divided by Zero")
else:
    # else executed only when no exception is thrown
    print("No exception is thrown")

# handling different exception

try:
    age = int(input("Enter the age: "))
    xfact = 10/age
except (ValueError, ZeroDivisionError):
    print("You can't divide by zero")
except ZeroDivisionError:      # here this except clause in not going to executed
    print("you canot divide by zero")
else:
    print("All goes fine")
