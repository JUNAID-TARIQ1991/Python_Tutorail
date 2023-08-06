def main():
    file = open('sale.dat', 'w')
    days = int(input("How many days y0u have worked :  >"))

    for count in range(1, days+1):
        sales = float(input("Enter the sale for day" + " #" + str(count)+": "))
        write = "sale of day #" + str(count) + ": "
        file.write(write + str(sales) + '\n')
    file.close()


main()
