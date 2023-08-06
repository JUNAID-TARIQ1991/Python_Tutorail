
try:
    file = open('test.py', 'w')
    # if there is exception at this line, the following lines will
    age = int(input("Enter the age: "))
    'not executed'
    xfact = 10/age
except (ValueError, ZeroDivisionError):
    print("You can't divide by zero")
except ZeroDivisionError:      # here this except clause in not going to executed
    print("you canot divide by zero")
else:
    print("All goes fine")
finally:
    # file always close if there is exception in the progeam or not.
    file.close()
