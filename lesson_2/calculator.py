# # Take two numbers from input
# # Ask the user for the type of operation: addition, subtraction,
# #     multiplication, or division
# # Perform the calculation and display the result

print("Welcome to the calculator")
num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))
operation = int(input("Please enter the number of the operation you would "
                        "like to perform\n1. Addition\n2. Subtraction\n"
                        "3. Multiplication\n4. Division\n"))

def calculator(number1, number2, op_type):
    match op_type:
        case 1:
            return number1 + number2
        case 2:
            return number1 - number2
        case 3:
            return number1 * number2
        case 4:
            return number1 / number2
        case _:
            return 'Error, invalid operation'

print(f'The result is: {calculator(num1, num2, operation)}')
