#!/usr/bin/python3
from datetime import datetime as dt

def Dating():
    """defines the module of the file"""
    age = int(input("Enter your birth year here to get your current age: "))
    today = dt.now()
    done = today.year - age
    print(f"Your current age is: {done}")

if __name__ == "__main__":
    Dating()
print("\nCode dveeloped by Masino")
