"""
A slightly refactored version of the RPS program after doing the lesson.
"""

import random
import os

VALID_CHOICES = ["Rock", "Paper", "Scissors"]

def prompt(message):
    print(f'==> {message}')

def player_pick():
    prompt("""Player, enter the corresponding number to make your choice """
            """(i.e. Rock = 1): \n"""
            """1. Rock\n"""
            """2. Paper\n"""
            """3. Scissors"""
            )
    choice = input()

    match choice:
        case "1":
            choice = VALID_CHOICES[0]
        case "2":
            choice = VALID_CHOICES[1]
        case "3":
            choice = VALID_CHOICES[2]

    while choice not in VALID_CHOICES:
        prompt("""Please enter a valid choice """
            """(i.e. Rock = 1): \n"""
            """1. Rock\n"""
            """2. Paper\n"""
            """3. Scissors"""
            )
        choice = input()

        match choice:
            case "1":
                choice = VALID_CHOICES[0]
            case "2":
                choice = VALID_CHOICES[1]
            case "3":
                choice = VALID_CHOICES[2]

    return choice

def computer_pick():
    return random.choice(VALID_CHOICES)

def determine_win(player, computer):
    prompt(f'''You chose {player}, the computer chose '''
    f'''{computer}.''')

    match player, computer:
        case "Rock", "Scissors":
            return f'{player} beats {computer}. The player wins!'
        case "Scissors", "Paper":
            return f'{player} beats {computer}. The player wins!'
        case "Paper", "Rock":
            return f'{player} beats {computer}. The player wins!'
        case "Rock", "Paper":
            return f'{computer} beats {player}. The computer wins!'
        case "Paper", "Scissors":
            return f'{computer} beats {player}. The computer wins!'
        case "Scissors", "Rock":
            return f'{computer} beats {player}. The computer wins!'
        case _:
            return f'Both players chose {player}. It\'s a tie!'

def play_again():
    prompt("Play again? y/n")
    play = input()
    while play not in ['y', 'n', 'Y', 'N']:
        prompt("Please enter a valid answer (y or n)")
        play = input()
    return play.lower()

while True:
    player_choice = player_pick()
    computer_choice = computer_pick()
    winner = determine_win(player_choice, computer_choice)
    prompt(winner)

    answer = play_again()

    if answer == 'y':
        os.system('clear')
    else:
        break
