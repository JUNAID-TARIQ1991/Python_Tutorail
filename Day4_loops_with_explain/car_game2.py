started = False
while True:
    command = input(">").upper()

    if command == 'HELP':
        print(
"""type start/START - to start the car\n
type stop/STOP - to stop the car\n
type quit/QUIT - exit the game """)
    elif command == 'START':
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car started! ready to go....")
    elif command == 'STOP':
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car stopped! take some rest")
    elif command == 'QUIT':
        break
    else:
        print("I don't understand That")
