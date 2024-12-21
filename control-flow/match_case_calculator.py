#!/usr/bin/env python3

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

num1 = int(num1)
num2 = int(num2)


operation = input("Choose the operation (+, -, *, /): .")

match operation:
    case "+":
        result = num1 + num2
        print(f'The result is {result}')
    case "-":
        result = num1 - num2
        print(f'The result is {result}')
    case "*":
        result = num1 * num2
        print(f'The result is {result}')
    case "/":
        if num2 == 0:
            print("Division by zero is not allowed.")

        else:
            result = num1 / num2
            print(f'The result is {result}')
    case _:
        if num1 or num2 != int:
            print("Invalid day entered.")
