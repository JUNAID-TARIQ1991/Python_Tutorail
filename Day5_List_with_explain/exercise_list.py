largest_number=0
number=[1,2,4,6,9,10,14,6,24,98,65,39]
max=number[0]
for i in number:
    if i>largest_number:
        largest_number=i
print(largest_number)    

'''another method'''
for i in number:
    if i>max:
        max=i
print(max)