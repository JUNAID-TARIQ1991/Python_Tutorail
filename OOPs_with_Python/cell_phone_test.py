import CellPhone
def main():
    man = input("Enter the manufacturer: ")
    model = input("Enter the model: ")
    price = input("enter the retail Price: ")
# Create an instance/Object of the CellPhone class/module.
    phone=CellPhone.CellPhone(man,model,price)
# Display the data that was entered.
    print('Here is the data that you entered:')
    print("The manufact of phone is: ", phone.get_manufact())
    print("The Model of phone is: " , phone.get_model())
    print("The retail price of phone is $: ", format(phone.get_retail_price()))
main()
