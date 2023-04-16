#!/usr/bin/python3
"""
This Program add an Extra note to the raise exception
"""
def Error():
    try:
        raise TypeError("Bad Type Here")
    except Exception as e:
        e.add_note("Add more information")
        e.add_note("Add More")
        raise

Error()
print("\nCode developed by Masino")
