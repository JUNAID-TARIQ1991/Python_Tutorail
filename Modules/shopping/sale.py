
total_sale = 100
print(__name__)


def calc_tax():
    print("Calculating tax")
    tax = total_sale * 0.1
    return tax


def calc_shipping():
    shipping = total_sale - 20


# This piece/block of code will not execute in the module where this module is imported
if __name__ == "__main__":
    print("Sale started")
    print("Sale module inialized", __name__)
    print(calc_tax())
