#!/usr/bin/env python3
import math

# Conversion formulas
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5 / 9)

def celsius_to_fahrenheit(celsius):
    return (celsius * (9 / 5)) + 32


try:
    temp = float(input("Enter the temperature to convert: "))
except ValueError:
    print("Please enter a valid number for temperature.")
    exit()


temp_c_or_f = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

if temp_c_or_f == 'F':
    temp_c = fahrenheit_to_celsius(temp)
    print(f"{temp}°F is equal to {temp_c:.2f}°C.")
elif temp_c_or_f == 'C':
    temp_f = celsius_to_fahrenheit(temp)
    print(f"{temp}°C is equal to {temp_f:.2f}°F.")
else:
    print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")


class TemperatureConverter:
    def __init__(self, temp, temp_type):
        self.temp = temp
        self.temp_type = temp_type

    def convert(self):
        if self.temp_type == 'C':
            return celsius_to_fahrenheit(self.temp)
        elif self.temp_type == 'F':
            return fahrenheit_to_celsius(self.temp)
        else:
            raise ValueError("Temperature type must be 'C' or 'F'.")
