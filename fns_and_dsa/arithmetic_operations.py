#!/usr/bin/env python3

def perform_operation(num1, num2, operation):
    """
    Perform the specified arithmetic operation on num1 and num2.

    :param num1: First number (float).
    :param num2: Second number (float).
    :param operation: The operation to perform ('add', 'subtract', 'multiply', 'divide').
    :return: The result of the operation or None in case of an error (e.g., invalid operation or division by zero).
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
            return
    else:
        return 
