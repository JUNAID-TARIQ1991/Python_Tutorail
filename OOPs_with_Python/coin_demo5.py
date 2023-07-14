import Coin


def main():
    coin1 = Coin.Coin()
    coin2 = Coin.Coin()
    coin3 = Coin.Coin()
    # Display the side of each coin that is facing up.
    print('I have three coins with these sides up:')
    print(coin1.get_side_up())
    print(coin2.get_side_up())
    print(coin3.get_side_up())
    


    print("I am going to toss these coins")
    print()
    print(coin1.toss())
    print(coin2.toss())
    print(coin3.toss())


    # Display the side of each coin that is facing up.
    print('Now here are the sides that are up:')
    print(coin1.get_side_up())
    print(coin2.get_side_up())
    print(coin3.get_side_up())
    print()
main()