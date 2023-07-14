import CellPhone


def main():
    # make a list of cell phones:
    #phones = make_list()
    Phones=make_list()
    # Display the data in the list.
    print("Here is the data you have entered")
    display_list(Phones)

# The make_list function gets data from the user
# for five phones. The function returns a list
# of CellPhone objects containing the data.


def make_list():
    phone_list = []
    print("enter the data of five phones:")
    for count in range(1, 6):
        print('Phone number ' + str(count) + ':')
        man = input("enter the manufact of phone:")
        model = input("enter the model of phone:")
        price = float(input("Enter the price of phone: "))
        print()
    # Create a new CellPhone object in memory and
    # assign it to the phone variable.
        phone = CellPhone.CellPhone(man, model, price)
        phone_list.append(phone)
    # Return the list.
    return phone_list


def display_list(phone_list):
    for item in phone_list:
        print(item.get_manufact())
        print(item.get_model())
        print(item.get_retail_price())
        print()


main()
