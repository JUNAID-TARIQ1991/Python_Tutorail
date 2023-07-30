list = [5,2,5,2,2]
for i in list:
    print("X"*i)

print("***************************")
list1=[2,2,2,2,7]
for i in list1:
    print("X"*i)
 
print("***************************")
'''Here is an another method'''
for x in list:
    output=''
    for count in range(x):
        output += 'x'
    print(output)
    