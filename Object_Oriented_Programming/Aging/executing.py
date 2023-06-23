#!/usr/bin/python3

"""
This module has the execution function for the age determination
"""

def execute():
    """defines the execution function"""
    from datetime import datetime as dt

    birth = int(input("Enter your birth year to determine your current age(ex: 2000): "))
    current = dt.now()
    today = current.year
    age = today - birth
    print(f"As at {today}, you are {age} years old")

if __name__ == "__main__":
    execute()
print("\nCode developed by Masino")
