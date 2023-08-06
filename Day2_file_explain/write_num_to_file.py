try:
    file = open('file2.dat', 'r')
except:
    print("The file is not present in the present directory")
    print("creating file.....")
    # file = open('file1.py')
else:
    print("file present")
number = 8


line1 = file.readline()
line2 = file.readline()
line3 = file.readline()
num1 = int(line1)
num2 = int(line2)
print(num1+num2)


file.close()
