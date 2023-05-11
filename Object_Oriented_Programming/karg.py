#!/usr/bin/python3

"""
This class uses 'karg' to multiply multiple numbers
"""
class Mul:

    def mul():
        items = input("Please enter numbers you want to multipy: ")
        items = items.split(" ")
        result = 1
        for item in items:
            item = int(item)
            result *= item
        print(result)

Mul.mul()
print("\nCode developed by Masino")
