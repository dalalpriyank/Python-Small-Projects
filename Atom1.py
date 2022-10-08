import string
started = False
stopped = False
while True:
    string = input(">>").lower()
    if string.lower() == "help":
        print("""
            start - to Start the car
            stop - to stop the car
            quit - to quit the car
        """)
    elif string == "start":
        if(started == True):
            print("Car already stated")
            stopped = False
        else:
            print("car is started")
            started = True
            stopped = False
    elif string == "stop":
        if(stopped == True):
            print ("car alrady stopped")
        else:
            stopped = True
            started = False
            print("Car stopped")
    elif string == "quit":
        print("your quit the car")
        break
    else:
        print("I don't understand - try 'Help' ")
