from sys import argv
script, file_name=argv
txt=open(file_name)
print(txt.read())
print("Write again the name of file you want to open?")
file_name=input('>')
txt=open(file_name)
print(txt.read())