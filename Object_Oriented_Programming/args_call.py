#!/usr/bin/python3

"""
This Funtion defines 'args' and uses it to call a function
"""

def Args(arg1, arg2, arg3, arg4):
    print("First:", arg1)
    print("Second:", arg2)
    print("Third:", arg3)
    print("Fourth:", arg4)
    args = ("Lime", "Garlic", "GingerBreadMan", "Orange Juice")
Args(*args)
print("Code developed by Masino")
