'''command = ''
while command.lower()!='quit':
    command=input(">")
    if command.upper()== 'HELP':
        print ("type start/START - to start the car\n")
        print("type stop/STOP - to stop the car\n")
        print('type quit/QUIT - exit the game')
    elif command.upper()=='START':
        print("Car sarted! ready to go....")
    elif command.upper()=='STOP':
        print("Car stopped! take some rest")
    elif command.upper()=='QUIT':
        break
    else:
        print("I don't understand That")
'''
'''Now look at the vesion below most simpler then above one.'''
print("**************")
check=''
while True:
    command=input(">").upper()
    
    if check == 'START' and command == 'START':
        print("Car is alredy started! what you want to do ?")
    elif check =="STOP" and command == 'STOP':
        print("Car is alredy stop! what you want to do ?")
    else:
        if command== 'HELP':
            print (
"""type start/START - to start the car\n
type stop/STOP - to stop the car\n
type quit/QUIT - exit the game """)
        elif command=='START':
            print("Car sarted! ready to go....")
            check= command
        elif command=='STOP':
            print("Car stopped! take some rest")
            check= command
        elif command=='QUIT':
            break
        else:
            print("I don't understand That")
    