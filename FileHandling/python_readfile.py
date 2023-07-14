
from sys import argv
script, filename = argv
txt=open(filename)
print(f"here is your file {filename}")
print(txt.read())
print("enter the file name again")
filename_again=input(">")
txt_again=open(filename_again)
print(txt_again.read())