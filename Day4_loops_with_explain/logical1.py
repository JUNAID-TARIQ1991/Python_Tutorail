name = input("Enter you name >\t")
if len(name)<5:
    print("Name must be at least five charecter long")
elif len(name)>20:
    print("Name can't greater then 20 character")
else:
    print("It is okay")