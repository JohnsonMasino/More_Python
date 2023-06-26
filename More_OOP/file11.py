#!/usr/bin/python3
#This file applies some do functions to the turtle cmd console

import cmd
import sys

class More_Console(cmd.Cmd):
    """defines the class of the turtle console"""
    intro = 'Welcome to advanced console. Enter "?" or "help" to explore commands'
    prompt = '(Turtle) '
    file = False

    def do_EOF(self, line):
        'Terminates the console'
        return True
    def do_say_name(self, name):
        'prints the entered name or a statement if no name is entered'
        if name:
            print(f"Hi {name}, welcome here")
        else:
            print("Hello...\nHow are you doing todays ?")
    def do_say_age(self, age):
        'prints your current age when you enter your birth year'
        from datetime import datetime as dt
        birth_year = int(input("Enter your birth year here: "))
        today_date = dt.now()
        today_year = today_date.year
        age = int(today_year) - birth_year
        print(f"Your current age is: {age} years old")
    def do_say_max(self, maximum):
        'select the maximum number from a list of entered numbers'
        numbers = input("Enter some numbers here to get the maximum")
        numbers = numbers.split()
        sorted_numbers = []
        try:
            for i in numbers:
                sorted_numbers.append(i)
            maximum = sorted_numbers[0]
            for i in sorted_numbers:
                if i > maximum:
                    maximum = i
            print(f"The maximum numbers is: {maximum}.")
        except Exception as e:
            print(e)
    def do_forward(self, amount):
        'moves the cursor forward to the specified amount'
        return True

if __name__ == "__main__":
    More_Console().cmdloop()
print("\nCode developed by Masino")
