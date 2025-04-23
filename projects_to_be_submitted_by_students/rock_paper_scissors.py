import random


def get_user_choice():
    choice = input("What's your choice? 'R' for rock, 'P' for paper, 'S' for scissors\n").lower()
    return choice



def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"]) 



def decide_winner(user , computer):
    if user == computer:
        return "It's a Tie!"
    elif (user == "r" and computer == "scissors") or (user == "s" and computer == "paper") or (user == "p" and computer == "rock"):
        return "You Win!"
    else:
        return "Computer wins!"
    



def play_game():
    print("Welcome to rock, paper, scissors!")
    user = get_user_choice()
    computer = get_computer_choice()

    print(f"You chose {user}")
    print(f"computer chose {computer}")

    result = decide_winner(user , computer)
    print(result)
    

play_game()


