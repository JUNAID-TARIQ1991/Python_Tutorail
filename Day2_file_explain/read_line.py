def main():
    file = open("sale.dat", "r")
    for line in file:
        print(line.rstrip('\n'))
        print(type(line))


main()
