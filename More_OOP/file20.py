#!/usr/bin/python3
"""
This file
"""

def Getting():
    """defines the function"""

    try:
        name = input("Enter your name here: ")
        age = int(input("Enter your age here: "))
        if (age / 3) == len(name):
            print("You are unique")
        else:
            print("Nothing to show")
    except Exception as m:
        print(str(m))
    finally:
        print("Code execution ended")

if __name__ == "__main__":
    Getting()
print("\nCode developed by Masino")
