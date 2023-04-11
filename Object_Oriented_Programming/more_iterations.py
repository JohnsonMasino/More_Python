#!/usr/bin/python3

"""
This function calls the ietration function without using the for loop.
"""

def luup():
    name = "Masino"
    done = iter(name)
    print(next(done), next(done), next(done), next(done), next(done), next(done), end="")
"""    print(next(done))
    print(next(done))
"""
luup()
print("\nCode developed by Masino")
