#!/usr/bin/python3

"""
This class uses 'kwargs' to save a list of keys and values
"""

class KeyVal:

    def more(*names, **persons):
        print(f"Hi!\nMy name is {names}")
        for attr, value in persons.items():
            print(f"My siblings are: {attr}: {value}")

KeyVal.more("Masino", "Ejima", First="Chisom", second="Obumneme")
print("\nCode developed by Masino")
