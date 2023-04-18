#!/usr/bin/python3

"""
Declares a dictionary of users and status
"""

def User():
    details = {"Name": "Masino", "Age": 25, "Occupation(s)": "Med Lab Sci./Software Engineering"}
    for user, status in details.items():
        print(f"{user}: {status}")
User()
print("\nCode developed by Masino")
