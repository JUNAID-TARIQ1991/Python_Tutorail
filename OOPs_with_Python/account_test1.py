import Bank_account
# with the _ _str_ _ method added to it.
def main():
    #get the starting balance
    start_bal= float(input("Enter your starting balance: "))
    #create a object of BankAccount class
    saving=Bank_account.BankAccount(start_bal)
    # Deposit the user's paycheck.
    pay=float(input("how much you were paid this week? "))
    print("I will deposit that into your account.")
    saving.deposit(pay)
    # Display the balance.
    print('Your account balance is $',format(saving.getbalance(), ',.2f'),sep='')
    # Get the amount to withdraw.
    cash=float(input("How much amount would you like to withdraw ?"))
    print('I will withdraw that from your account.')
    saving.withdraw(cash)
    # Display the balance.
    #print('Your account balance is $',format(saving.getbalance(), ',.2f'),sep='')
    
    # Display the balance.
    print(saving)
main()