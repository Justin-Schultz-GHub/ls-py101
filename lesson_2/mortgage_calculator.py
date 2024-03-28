"""
A simple mortgage calculator.
Originally, I made 3 functions to check if the loan amount, interest rate,
and loan duration were valid, but in the end I realized I used the same logic
for each of them. I thought about refactoring the program to use one function
for all 3 checks, but figured it was better to leave it like this in case I
wanted to change the check logic for one value and not all.
"""
import os

def prompt(message):
    print(f'==> {message}')

def invalid_loan(amount):
    if float('-inf') < float(amount) < float('inf'):
        try:
            float(amount)
        except ValueError:
            return True

        return float(amount) <= 0

    else:
        return True

def invalid_int(pct):
    if float('-inf') < float(pct) < float('inf'):
        try:
            float(pct)
        except ValueError:
            return True

        return float(pct) < 0

    else:
        return True

def invalid_dur(duration):
    if float('-inf') < float(duration) < float('inf'):
        try:
            float(duration)
        except ValueError:
            return True

        return float(duration) <= 0

    else:
        return True

def get_loan_amount():
    prompt("Please enter your loan amount. (e.g. $250,000 = 250000)")
    amount = input()

    while invalid_loan(amount):
        prompt("Please enter a valid amount. (e.g. $250,000 = 250000)")
        amount = input()

    return float(amount)

def get_int_rate():
    prompt("Please enter an interest rate. (e.g. 6.5% = 6.5)")
    int_rate = input()

    while invalid_int(int_rate):
        prompt("Please enter a valid interest rate. (e.g. 6.5% = 6.5)")
        int_rate = input()

    return float(int_rate)

def get_loan_duration():
    prompt("Please enter the loan duration in years.")
    loan_duration = input()

    while invalid_dur(loan_duration):
        prompt("Please enter a valid duration.")
        loan_duration = input()

    return float(loan_duration)

def compute_monthly_payment(loan, rate, duration):
    if rate != 0:
        return round(loan * (((rate / 100) / 12) / (1 - (1 + ((rate / 100) / 12))
                    ** (-duration * 12))), 2)
    else:
        return round(loan / (duration * 12), 2)

def display_result(amount, rate, duration, payment):
    prompt(f'''With a loan amount of ${amount}, an interest rate of '''
    f'''{rate}%, and a duration of {duration} years, your monthly '''
    f'''payment is: ${payment}''')

def perform_new_calc():
    prompt("Would you like to calculate another loan? y/n")
    try_again = input()
    while try_again not in ['y', 'n', 'Y', 'N']:
        prompt("Please enter a valid answer (y or n)")
        try_again = input()
    return try_again.lower()

while True:
    loan_amount = get_loan_amount()
    int_rate = get_int_rate()
    loan_duration = get_loan_duration()
    monthly_payment = compute_monthly_payment(
                    loan_amount, int_rate, loan_duration
                    )
    display_result(loan_amount, int_rate, loan_duration, monthly_payment)


    answer = perform_new_calc()

    if answer == 'y':
        os.system('clear')
    else:
        break
