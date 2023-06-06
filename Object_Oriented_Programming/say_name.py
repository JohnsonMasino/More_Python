#!/usr/bin/python3

"""
This file prints the name of a user
"""

class SayName:
    """defines the class of the module"""

    def say_name():
        """defines the class of the module"""
        name = input("Hi!\nPlease let us know your name here: ")
        try:
            print(f"Welcome here {name}")
        except ValueError:
            print("Value error identified...")
        except Exception as e:
            print("Check your code for possible errors")
        finally:
            print("No error in this code...")

if __name__ == "__main__":
    SayName.say_name()
print("\nCode developed by Masino")
