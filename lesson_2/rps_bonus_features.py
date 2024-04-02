"""
RPS with bonus features. Using Global statement which is pretty bad, but I'm
not sure what the better way to increment is.
"""

import random
import os

VALID_CHOICES = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
SCORE_LIMIT = 5
WINNING_COMBOS = {
    'Rock':     ['Scissors', 'Lizard'],
    'Paper':    ['Rock',     'Spock'],
    'Scissors': ['Paper',    'Lizard'],
    'Lizard':   ['Paper',    'Spock'],
    'Spock':    ['Rock',     'Scissors'],
}

def prompt(message):
    print(f'==> {message}')

def player_pick():
    prompt("""Player, enter the corresponding number to make your choice """
            """(i.e. Rock = 1): \n"""
            """1. Rock\n"""
            """2. Paper\n"""
            """3. Scissors\n"""
            """4. Lizard\n"""
            """5. Spock"""
            )
    choice = input()

    match choice:
        case "1":
            choice = VALID_CHOICES[0]
        case "2":
            choice = VALID_CHOICES[1]
        case "3":
            choice = VALID_CHOICES[2]
        case "4":
            choice = VALID_CHOICES[3]
        case "5":
            choice = VALID_CHOICES[4]

    while choice not in VALID_CHOICES:
        prompt("""Please enter a valid choice """
            """(i.e. Rock = 1): \n"""
            """1. Rock\n"""
            """2. Paper\n"""
            """3. Scissors\n"""
            """4. Lizard\n"""
            """5. Spock"""
            )
        choice = input()

        match choice:
            case "1":
                choice = VALID_CHOICES[0]
            case "2":
                choice = VALID_CHOICES[1]
            case "3":
                choice = VALID_CHOICES[2]
            case "4":
                choice = VALID_CHOICES[3]
            case "5":
                choice = VALID_CHOICES[4]

    return choice

def computer_pick():
    return random.choice(VALID_CHOICES)

def player_wins(player, computer):
    return computer in WINNING_COMBOS[player]

def computer_wins(player, computer):
    return player in WINNING_COMBOS[computer]

def tie_checker(winner1, winner2):
    return winner1 == winner2

def play_again():
    prompt("Play again? y/n")
    play = input()
    while play not in ['y', 'n', 'Y', 'N']:
        prompt("Please enter a valid answer (y or n)")
        play = input()
    return play.lower()

player_score = 0
computer_score = 0

def score_keeper(winner, player, computer):
    global player_score
    global computer_score

    if winner:
        prompt(f'{player} beats {computer}! Player +1!')
        player_score += 1
    elif not winner:
        if not tie_checker(player_wins(player_choice, computer_choice),
            computer_wins(player_choice, computer_choice)):
            prompt(f'{computer} beats {player}! Computer +1!')
            computer_score += 1
        else:
            prompt(f'Both players chose {player}.')

def score_announce(score1, score2):
    if score1 < SCORE_LIMIT and score2 < SCORE_LIMIT:
        return f'The score is {score1} to {score2}.'

    if score1 > score2:
        return f'The player wins! Final score: {score1} to {score2}.'

    return f'The computer wins! Final score: {score1} to {score2}.'

game_round = 0

def round_announce():
    global game_round

    if game_round != 0:
        print('')

    game_round += 1
    return prompt(f'Round {game_round}')

def pick_announce(player, computer):
    prompt(f'''You chose {player}, the computer chose '''
    f'''{computer}.''')

while True:
    round_announce()
    player_choice = player_pick()
    computer_choice = computer_pick()
    pick_announce(player_choice, computer_choice)
    round_winner = player_wins(player_choice, computer_choice)
    score_keeper(round_winner, player_choice, computer_choice)

    tie_checker(
        player_wins(player_choice, computer_choice),
        computer_wins(player_choice, computer_choice)
        )

    prompt(score_announce(player_score, computer_score))

    if player_score >= SCORE_LIMIT or computer_score >= SCORE_LIMIT:
        answer = play_again()

        if answer == 'y':
            player_score = 0
            computer_score = 0
            game_round = 0
            os.system('clear')
        else:
            break
