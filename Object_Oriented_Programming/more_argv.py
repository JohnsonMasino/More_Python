#!/usr/bin/python3

"""
This Program accepts multiple arguments at runtime
"""

class Arguments:
    def More_Argv(self, *ags):
        print("This is the first argument: ", self)
        for argument in ags:
            print("From more arguments we have: ", argument)
Arguments.More_Argv("Self", "Mango", "Orange", "Groundnut", "Final Item")
print("\nCode developed by Masino")
