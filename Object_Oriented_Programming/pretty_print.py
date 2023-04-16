#!/usr/bin/python3

"""
This program uses pretty printing
"""
import json as js

def JSON():
    print(js.dumps({"1": "Male", "0": "Female", "2": "TransGender"}, sort_keys=True, indent=1))
JSON()
print("\nCode developed by Masino")
