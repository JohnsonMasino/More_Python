#!/usr/bin/python3

"""
This program calls a funtion from 'mul.py' file
"""
from mul import ml as m

def numbers():
    num = input("Enter two numbers to be multiplied and separate with a space: ")
    num = num.split(' ')
    return m(int(num[0]), int(num[1]))
print(numbers())
print("\ncode developed by Masino")
