#!/usr/bin/python3
"""
This class defines a robot abd
retuns some futures of it.
"""
class Robotic:
    count = 0

    def __init__(self, name, id_number):
        """Initialising data"""
        self.name = name
        self.id_number = id_number

    def say_name(self):
        print("Hi, My name is: ", self.name)

    def say_num(self):
        print("My id number is: ", self.id_number)
#        print(f"We are only {count} here")

Robotic("Deca-6D17", "64-BD-2020").say_name()
Robotic("64-BD-2020", "64-BD-2020").say_num()
print('\n')
Robotic("Soni-BB25", "91-PQ-2020").say_name()
Robotic("Soni-BB25", "91-PQ-2020").say_num()
print("\nCode developed by Masino")
