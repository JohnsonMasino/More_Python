#!/usr/bin/python3

"""
This file finds out the age of a person using
the execute function from the executing module
"""
from executing import execute as ex

def Say_age():
    """prints the age of the user"""
    name = input("Welcome to KNOW AGE!\nWhat is your name please? ")
    year = int(input(f"Hi {name}!\nTell us the year you were born please... "))
    age = ex(year)
    try:
        print(f"{name}! your age as of 2023 is: {age}\nThank you!!!")
    except Exception as e:
        print("There's an exception error detected")
    finally:
        print("Code working fine")

if __name__ == "__main__":
    Say_age()
print("\nCode developed by Masino")
