#!/usr/bin/python3

"""
This function sorts keys in a JSON file
"""

def JSON():
    import json as js
    print(js.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))
    print(js.dumps({"d": 8, "c": 8, "b": 8, "a": 0}, sort_keys=True))
JSON()
print("\nCode developed by Masino")
