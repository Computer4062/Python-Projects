import random

s = ""

while s != "N":
    
    a = random.randint (1,5)
    b = random.randint (1,10)
    print ("-----------------------------")
    print ("G U E S S  T H E  N U M B E R")
    print ("-----------------------------")
    print ("Select your level")
    print ("A : Guess numbers from 1 to 5")
    print ("B : Guess numbers from 1 to 10")
    choice = input ("Enter your selected choice here:")

    def a_correct():
        if d == a:
            print ("You guessed it right")
        else:
            if d != a:
                print ("You guessed it wrong it is",a)

    def b_correct ():
        if f == b:
            print ("You guessed it right")
        else:
            if f != b:
                print ("You guessed it wrong it is",b)
                
    
    if choice == "A":
        print ("--------------------------")
        print ("Guess a number from 1 to 5")
        print ("--------------------------")
        d = int (input (":"))
        a_correct()
    else:
        if choice == "B":
            print ("----------------------------")
            print ("Guess a number from 1 to 10:")
            print ("----------------------------")
            f = int (input (":"))
            b_correct()

    
