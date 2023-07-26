discount_percent = 0.20


def get_reg_price():
    reg_price = float(input("Enter the reguar price ot produce: "))
    return reg_price


def discount_price(price):
    sale_price = price-(price*discount_percent)
    return sale_price


def main():
    reg_price = get_reg_price()
    sale_price = discount_price(reg_price)
    print('The sale price is $', format(sale_price, ',.2f'), sep='')


main()

'''This Python code defines a simple program to calculate the sale price of a product with a fixed discount percentage. Let's go through the code step by step:

discount_percent = 0.20: This line sets the value of discount_percent to 0.20, representing a 20% discount. You can change this value to apply a different discount rate if needed.

get_reg_price(): The get_reg_price() function prompts the user to enter the regular price of the product and returns the entered value as a floating-point number.

discount_price(price): The discount_price() function takes the regular price of the product (price) as an argument and calculates the sale price after applying the discount. 
It multiplies the price by discount_percent (20% in this case) and subtracts the resulting discount from the price, 
giving the final sale price. The calculated sale price is then returned.

main(): The main() function is the entry point of the program. It calls get_reg_price() to get the regular price from the user.
Then, it calls discount_price() with the regular price as an argument to calculate the sale price. Finally, it prints the calculated sale price using format() 
to display it with two decimal places and separated by commas.'''
