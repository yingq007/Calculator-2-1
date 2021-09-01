"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code


# repeat forever: --> while True
while True:
    input_string = input("> ") #User inputs: "+ 1 2"

    tokens = input_string.split(' ')
    
    if tokens[0] == "q":
        break

    num1 = float(tokens[1])

    if len(tokens) == 3:
        num2 = float(tokens[2])

    elif tokens[0] == "+":
        print(add(num1, num2))
    elif tokens[0] == "-":
        print(subtract(num1, num2))
    elif tokens[0] == "*":
        print(multiply(num1, num2))
    elif tokens[0] == "/":
        print(divide(num1, num2))
    elif tokens[0] == "square":
        print(square(num1))
    elif tokens[0] == "cube":
        print(cube(num1))
    elif tokens[0] == "pow":
        print(power(num1, num2))
    elif tokens[0] == "mod":
        print(mod(num1, num2))