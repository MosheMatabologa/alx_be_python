#!/usr/bin/env python3
import math


num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))
operation = input('Enter the operation (add, subtract, multiply, divide): ').strip().lower()


def perform_operation(num1: float, num2: float, operation: str) -> float:
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            raise ZeroDivisionError("Cannot divide by zero.")
    else:
        raise ValueError(f"Invalid operation: {operation}")

if __name__ == "__main__":
    try:
        result = perform_operation(num1, num2, operation)
        print(f"The result of {operation}ing {num1} and {num2} is: {result}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except ZeroDivisionError as zde:
        print(f"Error: {zde}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

