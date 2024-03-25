def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

prompt("Welcome to the calculator")

prompt("Please enter the first number:")
num1 = input()

while invalid_number(num1):
    prompt("Please enter a valid number")
    num1 = input()


prompt("Please enter the second number:")
num2 = input()

while invalid_number(num2):
    prompt("Please enter a valid number")
    num2 = input()

prompt("Please enter the number of the operation you would "
        "like to perform\n1. Addition\n2. Subtraction\n"
        "3. Multiplication\n4. Division")
operation = input()

while operation not in ['1', '2', '3', '4']:
    prompt("Please enter a valid number\n"
            "1. Addition\n2. Subtraction\n"
            "3. Multiplication\n4. Division")
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
        OUTPUT_OP = 'plus'
    case '2':
        OUTPUT_OP = 'minus'
    case '3':
        OUTPUT_OP = 'times'
    case '4':
        OUTPUT_OP = 'divided by'


prompt(f'The result of {num1} {OUTPUT_OP} {num2} is: {OUTPUT}')
