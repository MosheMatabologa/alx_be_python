#!/usr/bin/env python3

numerator = float(input("Enter the numerator: "))
denominator = float(input("Enter the denominator: "))

def safe_divide(numerator, denominator):
    try:
        return numerator / denominator
    except ZeroDivisionError:
        return print("Error: Cannot divide by zero.")
    except ValueError:
        if numerator == str or denominator == str:
            return ValueError
        print("Error: Please enter numeric values only.")
    finally:
        if numerator != 0:
            return
        print("Division is done.")
    
if __name__ == "__main__":
        #num1 = float(input("Enter the numerator: "))
        #num2 = float(input("Enter the denominator: "))
        result = safe_divide(numerator, denominator)
        if result is not None:
            print(f"The result is: {result}")   
