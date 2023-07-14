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