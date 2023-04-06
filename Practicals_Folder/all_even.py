#!/usr/bin/python3

"""
This program sums all even
numbers from 1 to 100
"""
#Code by Masino.

count = 0
for num in range(1, 101):
    if num % 2 == 0:
        count = count + num
print(count)
print("\nCode developed by Masino")
