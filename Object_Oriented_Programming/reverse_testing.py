#!/usr/bin/python3
"""
This program reverses texts using the reversed function
"""

def Reverse():
#    name = reversed(name)
    name = reversed(input("Enter your name here: "))
    for letter in name:
        print(letter, end="")
Reverse()
print("\n\nCode developed by Masino")
