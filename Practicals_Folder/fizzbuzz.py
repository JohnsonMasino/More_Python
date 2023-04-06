#!/usr/bin/python3

"""
This program prints all the numbers from 1 to 100
with some statements on some numbers based on conditions.
"""
#Code by Masino

for number in range(0, 101):
    if number % 3 == 0 and number % 5 == 0:
        print(number, "is: Fizzbuzz")
    elif number % 5 == 0:
        print(number, "is: Buzz")
    elif number % 3 == 0:
        print(number, "is: Fizz")
    else:
        print(number)
print("\nCode developed by Masino")        
