secret_number=9
guess = int(input("Input a guess number b/w 1 to 9:>\t"))
attempts = 1

while guess != secret_number:
    if attempts<3:
        print("Guess again:\t")
        
        guess = int(input())
        if guess == secret_number:
            print("Good! you guess right")
            exit()
        else:
            attempts =attempts+1
    else:
        print("you failed") 
        exit()   
while guess == secret_number:
    print("Great! you guess right")
    exit();        
        