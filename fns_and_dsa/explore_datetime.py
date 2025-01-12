#!/usr/bin/env python3
import datetime

def display_current_datetime():
   
    current_date = datetime.datetime.now() 
    formatted_current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_current_date}")
    return current_date  # Return the current_date object for further use
    
def calculate_future_date(current_date):
    try:
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        future_date = current_date + datetime.timedelta(days=number_of_days)
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future date: {formatted_future_date}")
    except ValueError:
        print("Invalid input! Please enter an integer value for the number of days.")

if __name__ == "__main__":
  
    current_date = display_current_datetime()
    
    calculate_future_date(current_date)

