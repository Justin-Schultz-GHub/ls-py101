"""
My solo attempt at the rock paper scissors program.
The player chooses a value (1-3) which is converted to rock, paper, or
scissors, and the computer is assigned a random value from 1-3 which is then
converted in the same way, and the values are checked to determine the winner.
Could be better, but just wanted to do a rough solo run on my own.
"""

import math
import random
import os

def prompt(message):
    print(f'==> {message}')

def invalid_choice(choice):
    try:
        float(choice)
    except ValueError:
        return True

    if float(choice) not in [1.0, 2.0, 3.0]:
        return True

    return False


def player_choice():
    prompt("""Player 1, enter the corresponding number to make your choice """
            """(i.e. Rock = 1): \n"""
            """1. Rock\n"""
            """2. Paper\n"""
            """3. Scissors"""
            )
    choice = input()

    while invalid_choice(choice):
        prompt("""Please enter a valid choice """
            """(i.e. Rock = 1): \n"""
            """1. Rock\n"""
            """2. Paper\n"""
            """3. Scissors"""
            )
        choice = input()

    choice = int(choice)

    match choice:
        case 1:
            return "Rock"
        case 2:
            return "Paper"
        case 3:
            return "Scissors"

def computer_choice():
    choice = math.floor(random.randrange(1, 3))

    match choice:
        case 1:
            return "Rock"
        case 2:
            return "Paper"
        case 3:
            return "Scissors"

def determine_win(player_choice, computer_choice):
    match player_choice, computer_choice:
        case "Rock", "Rock":
            return "Both players chose rock. It's a tie."
        case "Rock", "Paper":
            return "Paper beats rock. The computer wins!"
        case "Rock", "Scissors":
            return "Rock beats scissors. The player wins!"
        case "Paper", "Rock":
            return "Paper beats rock. The player wins!"
        case "Paper", "Paper":
            return "Both players chose paper. It's a tie!"
        case "Paper", "Scissors":
            return "Scissors beats paper. The computer wins!"
        case "Scissors", "Rock":
            return "Rock beats scissors. The computer wins!"
        case "Scissors", "Paper":
            return "Scissors beats paper. The player wins!"
        case "Scissors", "Scissors":
            return "Both players chose scissors. It's a tie!"


def play_again():
    prompt("Play again? y/n")
    play = input()
    while play not in ['y', 'n', 'Y', 'N']:
        prompt("Please enter a valid answer (y or n)")
        play = input()
    return play.lower()

while True:
    choice1 = player_choice()
    choice2 = computer_choice()
    prompt(f'The computer chooses {choice2}!')
    winner = determine_win(choice1, choice2)
    prompt(winner)

    answer = play_again()

    if answer == 'y':
        os.system('clear')
    else:
        break