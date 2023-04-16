#!/usr/bin/python3

"""
This Program handles name and items in more arguments
"""

class KeyAndValue:
    def Key(self, **args):
        print("This is the first argument: ", self)
        if args is not None:
            for (key, value) in args.items():
                print(key + ":", value)

KeyAndValue.Key("Self", Name="Masino", Complexion="Fair", Net_Worth = "USD65,000,000.00")
print("\nCode developed by Masino")
