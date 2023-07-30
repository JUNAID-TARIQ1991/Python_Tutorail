from sys import argv
file=open('ptdata_lal.dat','r')
#data=file.read()
#print(data)
#file1=open('new_ptdata','w')
#file1.write(data)
#file.close()
#file1.close()
for each in file:
    print(each)
    '''The open command will open the file in the read mode and the for loop 
    will print each line present in the file.'''
with open('ptdata_lal.dat') as file:
    data=file.read()
    print(data)
with open('data.dat','r') as file1:
    data1=file1.readlines()
    for line in data1:
        word=line.split
        print(word)
file1.close()
    
    
    
 