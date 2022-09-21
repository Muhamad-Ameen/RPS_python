# just for fun
import random

choices = ["Rock", "Paper", "Scissors"]

player_point = 0
computer_point = 0

while True:
    computer = random.choice(choices)
    player = input("choice Rock Paper or Scissor:- ").capitalize()
    win = f"\033[32;1mYou win\033[m computer:-{computer} and you:-{player}"
    lose = f"\033[31;1mYou lose\033[0m computer:-{computer} and you:-{player}"
    if player == computer:
        print("\033[0;33mTie\033[0m .....")

    elif player == "Rock":
        if computer == "Scissors":
            print(win)
            player_point += 1
        else:
            print(lose)
            computer_point += 1
    elif player == "Paper":
        if computer == "Rock":
            print(win)
            player_point += 1
        else:
            print(lose)
            computer_point += 1

    elif player == "Scissor":
        if computer == "Paper":
            print(win)
            player_point += 1
        else:
            print(lose)
            computer_point += 1
    elif player == "End":
        print(f"--Results--\ncomputer score = {computer_point}\nYour score = {player_point}")
        if computer_point > player_point:
            print("\033[31;1mYou Lose :(")
        elif computer_point < player_point:
            print("\033[32;1mCongratulations you win :)")
        else:
            print("\033[0;33mTie 😐")
        break

    else:
        print("Please choice Rock Paper or Scissor")
