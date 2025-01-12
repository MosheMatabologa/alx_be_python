#!/usr/bin/env python3

def perform_operation(num1: float, num2: float, operation: str):
    """
    Perform the specified arithmetic operation on num1 and num2.

    :param num1: First number (float).
    :param num2: Second number (float).
    :param operation: The operation to perform ('add', 'subtract', 'multiply', 'divide').
    :return: The result of the operation or a message in case of errors (e.g., division by zero).
    """
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
            return "Error: Cannot divide by zero."
    else:
        return "Error: Invalid operation. Please use 'add', 'subtract', 'multiply', or 'divide'."

