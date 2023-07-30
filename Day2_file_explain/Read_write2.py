from sys import argv
from os.path import exists
script_name, From_file, to_file=argv
print(f"we are going to copy the content of {From_file} to {to_file}")
data_from=open(From_file)
in_data=data_from.read()
print(f'Is the destination file {to_file} exist? {exists(to_file)}')
print('Ready! hit enter else hit ctrl-c')
input()
data_to=open(to_file,'w')
data_to.write(in_data)
data_from.close()
data_to.close()

