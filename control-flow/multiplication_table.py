#!/usr/bin/env python3

number = int(input("Enter a number to see its multiplication table: "))
X = number
for Y in range(1, 11):
    Z = number * Y
    print(f'{number} * {Y} = {Z}')
