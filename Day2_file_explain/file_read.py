def main():
    file = open('ptdata_lal.dat', 'r')

    line1 = file.readline()
    line2 = file.readline()
    line3 = file.readline()
    print(line1)
    print(line2)
    print(line3)

    line1 = line1.rstrip('\n')
    line2 = line2.rstrip("\n")
    line3 = line3.rstrip('\n')

    print(line1)
    print(line2)
    print(line3)
    file.close()


main()
