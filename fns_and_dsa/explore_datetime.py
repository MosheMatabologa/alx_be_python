#!/usr/bin/env python3
from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in the format 'YYYY-MM-DD HH:MM:SS'.
    """
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")
    return current_date

def calculate_future_date():
    """
    Prompts the user for a number of days and calculates the future date.
    """
    try:
        # Prompt for number of days as integer
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        # Calculate future date
        future_date = datetime.now() + timedelta(days=number_of_days)
        print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    except ValueError:
        print("Invalid input! Please enter an integer value for the number of days.")

if __name__ == "__main__":
    # Part 1: Display current date and time
    display_current_datetime()

    # Part 2: Calculate and display future date
    calculate_future_date()
