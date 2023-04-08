#!/usr/bin/python3

"""
This function forces a user to enter a username
"""

def user_name():
    num = input("Please enter your username here: ")
    if len(num) < 6:
        print("Sorry! less than expected characters")
    elif len(num) > 10:
        print("Sorry! More than required character")
    else:
        print("Thank You!")
user_name()
print("\nCode developed by Masino")        
