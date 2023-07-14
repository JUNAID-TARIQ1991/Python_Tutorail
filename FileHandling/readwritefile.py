#!/usr/bin/env python3
from sys import argv
script, file_name =argv
print(f"we are going to erase {file_name} ")
print("if you donot  want that hin ctrl-c (^c)")
print("if you want that hit return")
input("?")
print("opening file %s " %file_name)
target =open(file_name, 'w') # target verable open the file in write mode
print ("truncating the file good bye!")
target.truncate()
print("now i'm going to ask you some quetio?")
line1=input("line1:")
line2=input("line2:")
line3=input("line3:")
print(f"i'm going to write these to file {file_name}")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("finally we close it.")
target.close

