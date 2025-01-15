#!/usr/bin/env python3

def safe_divide(numerator, denominator):
    """Performs division safely, handling zero division and invalid inputs."""
    try:
        return numerator / denominator
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None

def main():
    try:
        # Convert inputs to floats directly to ensure proper types.
        numerator = (input("Enter the numerator: "))
        denominator = (input("Enter the denominator: "))
        float(numerator)
        float(denominator)

    except ValueError:
        print("Error: Please enter numeric values only.")
        return  # Exit early if invalid input is detected.

    result = safe_divide(numerator, denominator)
    if result is not None:
        print(f"The result of the division is {result:.1f}")

if __name__ == "__main__":
    main()

