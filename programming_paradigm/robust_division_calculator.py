#!/usr/bin/env python3

def safe_divide(numerator, denominator):
    try:
        return numerator / denominator
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None

if __name__ == "__main__":
    try:
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        float(numerator)
        float(denominator)

    except ValueError:
        print("Error: Please enter numeric values only.")
    else:
        result = safe_divide(numerator, denominator)
        if result is not None:
            print(f"The result is: {result}")
