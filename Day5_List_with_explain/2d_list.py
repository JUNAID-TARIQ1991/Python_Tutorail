'''In Python, a 2D list is a list of lists, where each element of the main list
is itself a list. It is also known as a list of lists. This data structure allows you to 
create a grid-like structure, where each element in the outer list represents a row, 
and each element in the inner lists represents a column.

To create a 2D list in Python, you can use the following syntax:'''
TD_list = [
    [1, 3, 4],
    [4, 7, 6],
    [4, 6, 8]
]


for row in TD_list:
    for element in row:
        print(element, end=' ')
    print()

'''This code initializes a 2D list called TD_list with three rows and three columns. Each row contains three elements (integers) within square brackets.

Next, the code uses nested loops to iterate through the 2D list and print its elements:

python
Copy code
for row in TD_list:
    for element in row:
        print(element, end=' ')
    print()
Here's how the nested loops work:

The outer loop (for row in TD_list:) iterates over each row in the TD_list. 
In the first iteration, row will be [1, 3, 4], in the second iteration, 
row will be [4, 7, 6], and in the third iteration, row will be [4, 6, 8].

The inner loop (for element in row:) iterates over each element in the current row.
In the first iteration of the outer loop, element will be 1, 3, and then 4. In the second iteration, element will be 4, 7, and then 6.
And in the third iteration, element will be 4, 6, and then 8.

Inside the inner loop, the print(element, end=' ') statement prints the current element 
followed by a space (the end=' ' argument ensures that each element is printed on the same line with a space separator).

After the inner loop completes printing all elements of the current row, the print() statement without any arguments is executed. This just prints a new line, effectively moving to the next row.'''
