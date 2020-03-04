import random

rand = random.randint(0, 15)

userInput = 0

while(userInput != rand):
    userInput = int(input("Pick a number in between 1 and 15: "))
    if(userInput < rand):
        print("Too low... try again...")
    elif(userInput > rand):
        print("Too high... try again")

if (userInput == rand):
    print("YOU GUESSED THE NUMBER!!!")
