#!/usr/bin/python3

"""
This file selects a random person to pay for a meal in a group of friends
"""

def Select():
    """function that selects a person at random to pay for a meal at a bar"""
    import random as rd

    try:
        names = input("Hi...!\nWelcome to person selector.\nEnter the names here: ")
        splitted_names = names.split()
        selected = rd.choice(splitted_names)
        print(f"For today, {selected} will pay the bill...")
    except Exception as e:
        print(__str__(e))
    finally:
        print("Code execution finished...")

if __name__ == "__main__":
    Select()
print("\nCode developed by Masino")
