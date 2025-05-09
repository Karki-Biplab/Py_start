# logo = """
#  _____________________
# |  _________________  |
# | | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------.
# | |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
# |  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
# | | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
# | |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
# | | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
# | |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
# | | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
# | |___|___|___| |___| | | |              | || |              | || |              | || |              | |
# | | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
# | |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------'
# |_____________________|
# """
#
#
# #Calculator
# print(logo)
#
# def add(n1, n2):
#     return n1 + n2
#
# def substraction(n1, n2):
#     return n1 - n2
#
# def multiplication(n1, n2):
#     return n1 * n2
#
# def divide(n1, n2):
#     return n1 / n2
#
#
#
# operations = {
#     "+": add,
#     "-": substraction,
#     "*": multiplication,
#     "/": divide
# }
#
# num1 = int(input("What is the first number? "))
# for symbol in operations:
#     print(symbol)
# operation_symbol = input("Pick an operation symbol from the line above: ")
# num2 = int(input("What is the second number? "))
# calculation_function = operations[operation_symbol]
# answer = calculation_function(num1, num2)
# print(f"{num1} {operation_symbol} {num2} = {answer}")
#
# operation_symbol = input("Pick an operation symbol from the line above: ")
# num3 = int(input("What is the   NEXT number? "))
# calculation_function = operations[operation_symbol]
# answer2 = calculation_function(calculation_function(num1, num2), num3)
# print(f"{num1, num2} {operation_symbol} {num3} = {answer2}")





logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


#Calculator
print(logo)

def add(n1, n2):
    return n1 + n2

def substraction(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2



operations = {
    "+": add,
    "-": substraction,
    "*": multiplication,
    "/": divide
}

num1 = float(input("What is the first number? "))
for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation symbol from the line above: ")
num2 = float(input("What is the second number? "))
calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")

while input("Do you wanna do these tasks again? (Y/N)") == "Y":
    operation_symbol = input("Pick an operation symbol from the line above: ")
    num2 = float(input("What is the   NEXT number? "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(answer, num2)
    print(f"{answer} {operation_symbol} {num2} = {answer}")
