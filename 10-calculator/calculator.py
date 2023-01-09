import os
import sys


def add(num1, num2):
    """
      Add two number and return results
    """
    return num1 + num2


def subtract(num1, num2):
    """
      Subtract two number and return results
    """
    return num1 - num2


def mudulo(num1, num2):
    """
     Divides the number and return the remainder
    """
    return num1 % num2


def divide(num1, num2):
    """
      Divide two number and return results
    """
    return num1 / num2


def multiply(num1, num2):
    """
      Multiply two number and return results
    """
    return num1 / num2


def clear():
    """
        clear console
    """
    os.system("cls")


def operator_input():
    """
        display operators
    """
    print("Select one of the operators")
    for operator in operators:
        print(operator)
    return input("")


def calculate(num1, num2):
    """
        return the sum after the operation
    """
    try:
        return operators[operator](num1, num2)
    except KeyError:
        sys.exit(f"{operator} is not a valid operator")


operators = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,
    "%": mudulo
}

from art import logo
print(logo)

try:
    # get integers and operator fro user
    num1 = int(input("Number1:"))
    operator = operator_input()
    num2 = int(input("Number2:"))

    # do calculation with the input 
    answer = calculate(num1, num2)
    # clear console
    clear()
    # display results
    print(f"{num1} {operator} {num2} = {answer}")
except ValueError as error:
    if ("invalid literal" in str(error)):
        sys.exit("Must be an integer")

# countine calculation
continue_calculation = True
while continue_calculation:
    continue_calculation = input("Do you want to continue? 'yes' or 'no'. ")

    # continue calculation if user types yes 
    if continue_calculation == "no":
        break
    else:
        continue_calculation = True

    # display operators
    operator = operator_input()

    # get new number  to perform math operation on it with the previous answer 
    try:
        num2 = int(input("Number2:"))
    except ValueError as error:
        if ("invalid literal" in str(error)):
            sys.exit("Must be an integer")

    prev_answer = answer
    answer = calculate(answer, num2)

    clear()

    print(f"{prev_answer} {operator} {num2} = {answer}")
