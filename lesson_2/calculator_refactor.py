import json
import os

def prompt(message):
    print(f'==> {message}')

def choose_language():
    os.system('clear')
    prompt("Please select the number of the language you would like to use.")
    prompt("1. English")
    prompt("2. 日本語")
    language = input()

    while language not in ["1", "2"]:
        prompt("Please select a valid number.\n")
        prompt("1. English")
        prompt("2. 日本語")
        language = input()

    match language:
        case "1":
            language_choice = "en"
            os.system('clear')
        case "2":
            language_choice = "jp"
            os.system('clear')

    return language_choice

with open ('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)[choose_language()]

prompt(MESSAGES["welcome"])

while True:
    def invalid_number(number_str):
        try:
            int(number_str)
        except ValueError:
            return True

        return False

    prompt(MESSAGES["first_num"])
    num1 = input()

    while invalid_number(num1):
        prompt(MESSAGES["enter_valid_num"])
        num1 = input()

    prompt(MESSAGES["second_num"])
    num2 = input()

    while invalid_number(num2):
        prompt(MESSAGES["enter_valid_num"])
        num2 = input()

    prompt(MESSAGES["prompt_op"])
    print(MESSAGES["valid_operation_num"])
    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt(MESSAGES["enter_valid_num"])
        print(MESSAGES["valid_operation_num"])
        operation = input()

    match operation:
        case '1':
            OUTPUT = int(num1) + int(num2)
        case '2':
            OUTPUT = int(num1) - int(num2)
        case '3':
            OUTPUT = int(num1) * int(num2)
        case '4':
            OUTPUT = int(num1) / int(num2)

    match operation:
        case '1':
            OUTPUT_OP = MESSAGES["plus"]
        case '2':
            OUTPUT_OP = MESSAGES["minus"]
        case '3':
            OUTPUT_OP = MESSAGES["times"]
        case '4':
            OUTPUT_OP = MESSAGES["divided_by"]

    prompt(f'{num1} {OUTPUT_OP} {num2} {MESSAGES["is"]}{OUTPUT}')

    prompt(MESSAGES["continue_calc"])
    calculate_ans = input()

    while calculate_ans not in ['y', 'n']:
        prompt(MESSAGES["enter_valid_y_n"])
        calculate_ans = input()

    if calculate_ans == 'y':
        os.system('clear')
    else:
        prompt(MESSAGES["no_continue"])
        os.system('clear')
        break
