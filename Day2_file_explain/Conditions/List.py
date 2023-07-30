#!/bin/usr/env python3
"""Here's what the code does, line by line:

ten_things = "Apples Oranges Crows Telephone Light Sugar": Creates a string of items separated by spaces and assigns 
it to the variable ten_things.

print "Wait there's not 10 things in that list, let's fix that.": Prints a message to the console.

stuff = ten_things.split(' '): Splits the string ten_things into a list of individual items, separated by spaces, and assigns it to the variable stuff.

more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]: Creates a new list of items and assigns it to the variable more_stuff.

while len(stuff) != 10:: Starts a loop that continues until the length of the stuff list is equal to 10.

next_one = more_stuff.pop(): Removes the last item from the more_stuff list and assigns it to the variable next_one.

print "Adding: ", next_one: Prints a message to the console indicating that the next_one item is being added to the stuff list.

stuff.append(next_one): Adds the next_one item to the end of the stuff list.

print "There's %d items now." % len(stuff): Prints a message to the console indicating the current number of items in the stuff list.

print "There we go: ", stuff: Prints the updated stuff list to the console.

print "Let's do some things with stuff.": Prints a message to the console.

stuff[1]: Accesses the item at index 1 of the stuff list and prints it to the console.

stuff[-1]: Accesses the last item in the stuff list and prints it to the console.

stuff.pop(): Removes the last item from the stuff list and returns it.

' '.join(stuff): Joins the items in the stuff list with a space separator and returns the resulting string.

'#'.join(stuff[3:5]): Joins the items in the slice of the stuff list from index 3 to index 5 (excluding index 5) 
with a # separator and returns the resulting string.

Overall, the code demonstrates various ways of working with lists in Python, including appending new items to a list, 
accessing items in a list, 
removing items from a list, and joining items in a list into a string.
"""
ten_things = "Apples Oranges Crows Telephone Light Sugar"
print("Wait there's not 10 things in that list, let's fix that.")
stuff = ten_things.split(' ')
print(stuff)
more_stuff = ["Day", "Night", "Song","Frisbee", "Corn", "Banana", "Girl", "Boy"]
while len(stuff) != 10:
    next_one = more_stuff.pop()
    print ("Adding: ", next_one)
    stuff.append(next_one)
    print ("There's %d items now." % len(stuff))
    print ("There we go: ", stuff)
    print ("Let's do some things with stuff.")

print(stuff[1])
print(stuff[- 1])  # whoa! fancy
print(stuff.pop())

