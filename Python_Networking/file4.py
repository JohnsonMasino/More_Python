#!/usr/bin/python3
"""
This file uses the get function to send requests
"""

def Getting():
    """defines the file function"""
    import requests

    try:
        container = {"Name": "Kings", "Complexion": "Dark", "Age": "17", "Net Worth": "USD10m"}
        name = requests.get("https://www.google.com", params="container")
        print(name.text)
        print(name.encoding)
        print(name.content)
    except Exception as m:
        print(str(m))
    finally:
        print("\nCode execution finished...")

if __name__ == "__main__":
    Getting()
print("\nCode developed by Masino")
