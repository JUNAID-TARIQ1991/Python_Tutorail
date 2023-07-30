from sys import argv 
script, file1=argv
data=open(file1, 'a')
data.write("This is the new line")
data.close()