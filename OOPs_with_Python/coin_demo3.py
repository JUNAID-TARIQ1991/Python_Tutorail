#!/usr/bin/env python3
import random
# The Coin class simulates a coin that can
# be flipped.
class Coin:
    #If we change the name of the sideup attribute
    # to _ _sideup , then code outside the Coin class will not be able to access it.
    def __init__(self):
        self.__side_up="head"
        
    def toss(self):
        if random.randint(0,1)==0:
            self.__side_up='head'
        else:
            self.__side_up='tail'    
        
    def get_side_up(self):
        return self.__side_up
    
def main():
    #Create an object from the Coin class.
    coin1 = Coin()
    print("This side is up ", coin1.get_side_up())
    print("I am tossing the coin ....")
    coin1.toss()
    print("This side is up ", coin1.get_side_up())

def main():
    #Create an object from the Coin class.
    coin1 = Coin()
    print("This side is up ", coin1.get_side_up())
    print("I am tossing the coin ....")
    for count in range(10):
        coin1.toss()
        print("This side is up ", coin1.get_side_up())
        
    
    
    ## But now I'm going to cheat! I'm going to
# directly change the value of the object's
# sideup attribute to 'Heads'.
    
    
main()
    
    
    
        