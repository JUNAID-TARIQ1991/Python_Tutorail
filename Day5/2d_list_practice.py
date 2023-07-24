list = [
    [1,5,8],
    [5,6,7],
    [5,6,7],
    [4,9,0]
]

#print(list[0][1])
for row in list:
    for element in row:
        print(element,  end=' ')
    print()
    
print("some more practice")
'''append(x): Adds an element x to the end of the list.
extend(iterable): Extends the list by appending elements from the iterable.
insert(i, x): Inserts element x at the specified index i.
remove(x): Removes the first occurrence of element x from the list.
pop([i]): Removes and returns the element at the given index i. 
If i is not provided, it removes and returns the last element.
clear(): Removes all elements from the list.
index(x[, start[, end]]): Returns the index of the first occurrence of 
element x in the list.
count(x): Returns the number of occurrences of element x in the list.
sort(key=None, reverse=False): Sorts the list in ascending order by default. 
key is an optional function to customize sorting, and reverse=True sorts the list in descending order.
reverse(): Reverses the elements of the list in place.
copy(): Returns a shallow copy of the list.'''
print("**********************************")
list=[1,4,6,7,8,9,3,0,3]
number=list[0]
print(number)
list.append(9)
print(list)
list.insert(0,4)
print(list)
list.pop()
print(list)
print(12 in list)
print(12 not in list) 
print(list.count(4))
list.sort() #asscending
print(list)
list.reverse() #descending
print(list)
list2=list.copy()
list.append(10)
print(list)
print(list2)
