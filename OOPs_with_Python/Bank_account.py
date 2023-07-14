#!/usr/bin/env python3
class BankAccount:
    # The _ _init_ _ method accepts an argument for
    # the account's balance. It is assigned to
    # the _ _balance attribute.
    def __init__(self, bal):
        self.__balance = bal
# The deposit method makes a deposit into the
# account.

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Error: insufficient balance ", (amount))
# The get_balance method returns the
# account balance.
    def getbalance(self):
        return self.__balance
    
# The _ _str_ _ method returns a string
# indicating the object's state.
    def __str__(self):
        return 'The balance is $' + format(self.__balance, ',.2f')
