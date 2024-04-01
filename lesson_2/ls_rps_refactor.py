import random

VALID_CHOICES = ["rock", "paper", "scissors"]

def prompt(message):
    print(f"==> {message}")

def player_pick():
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    choice = input()

    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        choice = input()

    return choice

def computer_choice():
    return random.choice(VALID_CHOICES)

def display_winner(player, computer):
    prompt(f"You chose {player}, computer chose {computer}")

    if ((player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")):
        prompt("You win!")
    elif ((player == "rock" and computer == "paper") or
          (player == "paper" and computer == "scissors") or
          (player == "scissors" and computer == "rock")):
        prompt("Computer wins!")
    else:
        prompt("It's a tie!")

def play_again():
    prompt("Do you want to play again (y/n)?")
    answer = input().lower()

    while answer == '' or (answer[0] != 'n' and answer[0] != 'y'):
        prompt('Please enter "y" or "n".')
        answer = input().lower()

    return answer

while True:
    player_choice = player_pick()
    computer_choice = computer_choice()
    display_winner(player_choice, computer_choice)

    play_again = list(play_again())

    if play_again[0] != "y":
        break
