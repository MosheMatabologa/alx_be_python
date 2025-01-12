#!/usr/bin/env python3

# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  # Explicitly defined as 9/5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main function for user interaction
def main():
    try:
        # Prompt user for temperature
        temp_input = input("Enter the temperature to convert: ")
        temp = float(temp_input)  # Convert input to float
        
        # Prompt user for the type of temperature
        temp_c_or_f = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        # Perform the appropriate conversion
        if temp_c_or_f == 'F':
            temp_c = convert_to_celsius(temp)
            print(f"{temp:.1f}°F is {temp_c:.2f}°C")
        elif temp_c_or_f == 'C':
            temp_f = convert_to_fahrenheit(temp)
            print(f"{temp:.1f}°C is {temp_f:.2f}°F")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError as e:
        print(f"Error: {e}")

# Run the script
if __name__ == "__main__":
    main()

