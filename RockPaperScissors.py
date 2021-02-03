import random

turns = int(input("enter the number of turns you want:"))
for i in range(0, turns):


    def RPC():

        user = input(f"write (R) for rock , (P) for paper and (S) for scissor").lower()
        computer = random.choice(['r', 'p', 's'])


        if user == computer:
            return "it's a tie "

        if is_win(user,computer):
            return "you won"
        else:
            return "you lost , computer won"


    def is_win(user,computer):

        if (user == 'r' and computer == 's') or ( user == 'p' and computer == 'r') or (user == 's' and computer == 'r') or (user == 's' and computer == 'p'):
            return True


    print(RPC())
