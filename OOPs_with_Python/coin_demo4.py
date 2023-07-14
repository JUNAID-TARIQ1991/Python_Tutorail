import Coin
def main():
    #Create an object from the Coin class.
    coin1 = Coin.Coin()
    print("This side is up ", coin1.get_side_up())
    print("I am tossing the coin ....")
    coin1.toss()
    print("This side is up ", coin1.get_side_up())
    
    #you can't do this here ?
    coin1.side_up='head'
    print("This side is up ", coin1.get_side_up())
    
    
    
    ## But now I'm going to cheat! I'm going to
# directly change the value of the object's
# sideup attribute to 'Heads'.
    
    
main()