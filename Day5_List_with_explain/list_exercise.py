my_list = [1, 4, 2, 5, 2, 8, 6, 0, 7, 7]

# Initialize a new list to store elements without consecutive duplicates
result_list = [my_list[0]]

# Iterate through the original list starting from the second element
for i in range(1, len(my_list)):
    if my_list[i] != my_list[i - 1]:  # Check for consecutive duplicates
        result_list.append(my_list[i])

print(result_list)


'''my_list[0]: This accesses the first element of the original list my_list.

[my_list[0]]: This constructs a new list with the first element of my_list as its only element.

result_list = [my_list[0]]: This assigns the newly created list (containing the first element of my_list)
to the variable result_list.

By doing this, we start building result_list with the first element of my_list, and then we'll add elements to it later, 
excluding consecutive duplicates.

For example, if my_list = [1, 4, 2, 5, 2, 8, 6, 0, 7, 7], then result_list is initialized as [1]. 
We then iterate through my_list and add non-consecutive duplicate elements to result_list, resulting in the final output [1, 4, 2, 5, 2, 8, 6, 0, 7], as demonstrated in the previous response.'''


print("***********************************NEXT METHOD*********************8")

numbers=[1,3,4,4,5,6,7,7,8,5,8,8]
unique=[]
for number in numbers:
    if number not in unique:
        unique.append(number)
        
print(unique)