import random
import time

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"print a number between 1 and {x} ="))
        if guess < random_number:
            print("that's too low dude , try again")
        elif guess > random_number:
            print("that's too high dude , you can try again tho ")
    print(f"yay dude , you did it , finally got {guess} which was the correct number ")

x=int(input())
print(guess(x))

def computerGuess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != 'c' :
        if low != high:
            guess = random.randint(low,high)
        elif low == high:
            guess = low

        feedback = input(f"is {guess} too low (L) , high (H) or correct (C)").lower()
        if feedback == 'l':
            low = guess + 1
        elif feedback == 'h':
            high = guess -1
    print(f"yay dude , you did it , finally got {guess} which was the correct number ")

x=int(input())
computerGuess(x)

