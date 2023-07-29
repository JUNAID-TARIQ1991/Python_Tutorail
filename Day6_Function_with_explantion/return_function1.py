def get_sale():
    total_sale = float(input("Enter the monthly sale of costomer: "))
    return total_sale


def adv_commision():
    commision = float(input("Enter the amount you received in advance: "))
    return commision


def commision_rate(sale):
    if sale <= 10000.0:
        rate = 0.1
    elif sale > 10000.0 and sale < 15000.0:
        rate = 0.15
    else:
        rate = 0.2
    return rate


def main():
    sale = get_sale()
    adv_comm = adv_commision()
    rate = commision_rate(sale)
    pay = sale * rate - adv_comm
    print("Your net pay will be :  $", pay)


main()
