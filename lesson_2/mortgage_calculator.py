"""
A simple mortgage calculator.
Originally, I made 3 functions to check if the loan amount, interest rate,
and loan duration were valid, but in the end I realized I used the same logic
for each of them. I thought about refactoring the program to use one function
for all 3 checks, but figured it was better to leave it like this in case I
wanted to change the check logic for one value and not all.
"""

def prompt(message):
    print(f'==> {message}')

def invalid_loan(amount):
    try:
        float(amount)
    except ValueError:
        return True

    return bool(float(amount) <= 0)

def invalid_int(pct):
    try:
        float(pct)
    except ValueError:
        return True

    return bool(float(pct) <= 0)

def invalid_dur(duration):
    try:
        float(duration)
    except ValueError:
        return True

    return bool(float(duration) <= 0)

while True:
    prompt("Please enter your loan amount. (e.g. $250,000 = 250000)")
    ln_amnt = input()

    while invalid_loan(ln_amnt):
        prompt("Please enter a valid amount.")
        ln_amnt = input()

    prompt("Please enter an interest rate. (e.g. 6.5% = 6.5)")
    int_rate = input()

    while invalid_int(int_rate):
        prompt("Please enter a valid interest rate.")
        int_rate = input()

    prompt("Please enter the loan duration in years.")
    ln_dur = input()

    while invalid_dur(ln_dur):
        prompt("Please enter a valid duration.")
        ln_dur = input()

    annual_int = float(int_rate) / 100
    mnthly_int = annual_int / 12
    ln_amnt = float(ln_amnt)
    mnths_dur = int(ln_dur) * 12
    mnthly_p = round(ln_amnt * (mnthly_int / (1 - (1 + mnthly_int)
                ** (-mnths_dur))), 2)

    prompt(f'''With a loan amount of ${ln_amnt}, an interest rate of '''
    f'''{int_rate}%, and a duration of {ln_dur} years, your monthly '''
    f'''payment is: ${mnthly_p}''')

    prompt("Would you like to calculate another loan? y/n")
    try_again = input()

    while try_again not in ['y', 'n']:
        prompt("Please enter a valid answer (y or n)")
        try_again = input()

    if try_again != 'y':
        break
