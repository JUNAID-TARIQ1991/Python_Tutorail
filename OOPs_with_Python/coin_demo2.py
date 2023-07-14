#!/usr/bin/env python3
import random
# The Coin class simulates a coin that can
# be flipped.
class Coin:
    def __init__(self):
        self.side_up="head"
        
    def toss(self):
        if random.randint(0,1)==0:
            self.side_up='head'
        else:
            self.side_up='tail'    
        
    def get_side_up(self):
        return self.side_up
    
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
    coin1.toss()
    
    
    ## But now I'm going to cheat! I'm going to
# directly change the value of the object's
# sideup attribute to 'Heads'.
    coin1.side_up='head'
    print("This side is up ", coin1.get_side_up())
    
main()
    
    
    
        