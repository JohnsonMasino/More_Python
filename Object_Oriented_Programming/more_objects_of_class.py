#!/usr/bin/python3

"""
This programme adds more objects to the class Ugwuanyi.
"""

class Ugwuanyi:
    count = 0

    def __init__(self, name):
        self.name = name
        print(f"Initialising {self.name}...")
    
    def greeting(self):
        print("Hi I am ", self.name)
        Ugwuanyi.count += 1
        print(f"There are {Ugwuanyi.count} persons here")

    def dying(self):
        Ugwuanyi.count -= 1
        print("Hi I am leaving this space now")
        if Ugwuanyi.count == 0:
            print("No one is left here\nGood bye")
        else:
            print(f"It is only {Ugwuanyi.count} persons that are remaining here")

person1 = Ugwuanyi("Chisom")
person1.greeting()
person2 = Ugwuanyi('Obum')
person2.greeting()
person1.dying()
person2.dying()
print("\nCode developed by Masino")
