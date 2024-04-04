"""
RPS with bonus features.
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

game_values = {
    "player_score": 0,
    "computer_score": 0,
    "game_round": 0,
}

def clear_screen():
    os.system('clear')

def prompt(message):
    print(f'==> {message}')

def start_game():
    clear_screen()
    def player_pick():
        prompt("""Player, enter the corresponding number to make your """
                """choice (i.e. Rock = 1): \n"""
                """1. Rock\n"""
                """2. Paper\n"""
                """3. Scissors\n"""
                """4. Lizard\n"""
                """5. Spock"""
                )
        choice = input()

        while choice not in ["1", "2", "3", "4", "5"]:
            prompt("""Please enter a valid choice """
                """(i.e. Rock = 1): \n"""
                """1. Rock\n"""
                """2. Paper\n"""
                """3. Scissors\n"""
                """4. Lizard\n"""
                """5. Spock"""
                )
            choice = input()

        choice = match_input_to_choice(choice)
        return choice

    def match_input_to_choice(player_input):
        match player_input:
            case "1":
                return VALID_CHOICES[0]
            case "2":
                return VALID_CHOICES[1]
            case "3":
                return VALID_CHOICES[2]
            case "4":
                return VALID_CHOICES[3]
            case "5":
                return VALID_CHOICES[4]

    def computer_pick():
        return random.choice(VALID_CHOICES)

    def player_wins(player, computer):
        return computer in WINNING_COMBOS[player]

    def computer_wins(player, computer):
        return player in WINNING_COMBOS[computer]

    def tie_checker(player, computer):
        return player == computer

    def play_again():
        prompt("Play again? y/n")
        play = input()
        while play not in ['y', 'n', 'Y', 'N']:
            prompt("Please enter a valid answer (y or n)")
            play = input()
        return play.lower()

    def score_keeper(winner, player, computer):
        if winner:
            prompt(f'{player} beats {computer}! Player +1!')
            game_values["player_score"] += 1
        elif not winner:
            if not tie_checker(player_wins(player_choice, computer_choice),
                computer_wins(player_choice, computer_choice)):
                prompt(f'{computer} beats {player}! Computer +1!')
                game_values["computer_score"] += 1
            else:
                prompt(f'Both players chose {player}.')

    def score_announce(score1, score2):
        if score1 < SCORE_LIMIT and score2 < SCORE_LIMIT:
            return f'The score is {score1} to {score2}.'

        if score1 > score2:
            return f'The player wins! Final score: {score1} to {score2}.'

        return f'The computer wins! Final score: {score1} to {score2}.'

    def round_announce():
        if game_values["game_round"] != 0:
            print('')

        game_values["game_round"] += 1
        if game_values["game_round"] == 1:
            return prompt(f'Round {game_values["game_round"]} - Best of 5')
        return prompt(f'Round {game_values["game_round"]}')

    def pick_announce(player, computer):
        prompt(f'''You chose {player}, the computer chose '''
        f'''{computer}.''')

    while True:
        round_announce()
        player_choice = player_pick()
        computer_choice = computer_pick()
        clear_screen()
        pick_announce(player_choice, computer_choice)
        round_winner = player_wins(player_choice, computer_choice)
        score_keeper(round_winner, player_choice, computer_choice)

        tie_checker(player_choice, computer_choice)

        prompt(
            score_announce(game_values["player_score"],
            game_values["computer_score"])
            )

        if (game_values["player_score"] >= SCORE_LIMIT or
        game_values["computer_score"] >= SCORE_LIMIT):
            answer = play_again()

            if answer == 'y':
                game_values["player_score"] = 0
                game_values["computer_score"] = 0
                game_values["game_round"] = 0
                clear_screen()
            else:
                clear_screen()
                break

start_game()
