#!/usr/bin/python3

def Say_Name():
    """defines the function of the module"""
    from datetime import datetime as dt

    try:
        name = input("Enter your name here: ")
        birth_year = int(input("Enter your birth year(ex: 1999) here: "))
        today = dt.now()
        today_year = today.year
        age = int(today_year) - birth_year
        print(f"The length of your name is: {len(name)}\nAnd you are {age} years old.")
    except Exception as e:
        print(f"Try again...\n{e}")
    finally:
        print("Code execution completed...")

if __name__ == "__main__":
    Say_Name()
print("\nCode developed by Masino")
