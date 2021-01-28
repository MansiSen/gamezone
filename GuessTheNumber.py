import random

def guess(x):
    rand = random.randint(1,x)
    guess = 0
    while guess != rand:
        guess = int(input())
        if guess < rand:
            print("sorry , guess again , it's too low")
        elif guess > rand:
            print("sorry , guess again , too high")
    print(f"congrats , you have hit the right number {rand}")


guess(5)