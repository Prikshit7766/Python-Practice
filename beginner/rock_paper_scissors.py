import random

def get_choices():
    player_choice=input("Enter your choice: (rock/paper/scissors) ")
    options=["rock","paper","scissors"]
    computer_choice=random.choice(options)
    choices ={"player_choice":player_choice,"computer_choice":computer_choice}

    return choices


def get_winner(choices):
    player_choice=choices["player_choice"]
    computer_choice=choices["computer_choice"]
    winner=""

    if player_choice == computer_choice:
        winner="Tie"
    elif player_choice == "rock":
        if computer_choice == "paper":
            winner="Computer"
        elif computer_choice == "scissors":
            winner="Player"
    elif player_choice == "paper":
        if computer_choice == "rock":
            winner="Player"
        elif computer_choice == "scissors":
            winner="Computer"
    elif player_choice == "scissors":
        if computer_choice == "rock":
            winner="Computer"
        elif computer_choice == "paper":
            winner="Player"

    return winner


def play():
    choices=get_choices()
    winner=get_winner(choices)
    print("You chose: "+choices["player_choice"])
    print("Computer chose: "+choices["computer_choice"])
    print("Winner: "+winner)



if __name__ == "__main__":
    play()
