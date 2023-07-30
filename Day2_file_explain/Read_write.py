'''• close – Closes the file. Like File->Save.. in your editor.
• read – Reads the contents of the file. You can assign the result to a variable.
• readline – Reads just one line of a text file.
• truncate – Empties the file. Watch out if you care about the file.
• write('stuff') – Writes ”stuff” to the file.
• seek(0) – Move the read/write location to the beginning of the file.'''
from sys import argv
script, file_name=argv
print(f"we are going to open {file_name}")
print(f"we will erase all data from file, if you don't hit ctrl-c, otherwise hit enter")
input=('?')
txt=open(file_name,'w',)
#print(txt.read())
print("Truncating! Good Bye")
txt.truncate()
txt.write("What are you doing sir \n")
txt.write("Why you donot learn to write programm")
txt.close()


