'''Is hot ia a boolean veriable. to initialize boolean we wrote is in the beginning'''
is_hot=False
is_cold=False
if is_hot:
    print("it's hot day outside")
    print("Drink Plantey of water")
elif is_cold:
    print("it is a cold day")
    print("wear warm clothes")
else:
    print("it is a pleasent day")
    print("enjoy your day")
'''Exercise'''
price=100000
has_good_credit=False
if has_good_credit:
    print("The customer need to pay 10% as credit")
    amount=(10/100)*price
    print(f"{amount}")
else:
    print("the customer need to pay 20% as credit")
    amount=(20/100)*price
    print(f"{amount}")