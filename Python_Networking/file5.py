#!/usr/bin/python3
"""
This file sends a post request
"""
import requests

def Posting():
    """defines the post request function"""

    try:
        box = {"Name": "Masino", "Net": "USD300m", "Age": 39 }
        name = requests.post("http://httpbin.org/post", data=box)
        print(name.text)
    except Exception as e:
        print(str(e))
    finally:
        print("Code execution finished...")

if __name__ == "__main__":
    Posting()
print("\nCode developed by Masino")
