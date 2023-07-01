#!/usr/bin/python3

"""Checks the syntax of using a dictionary"""
def Dict():
    """defines the function of dictionary"""
    import urllib.request
    import urllib.parse

    url = "https://pythonprogramming.net"
    container = {'Name':'Masino', 'Occupation':'Software Engineering'}
    for key, value in container.items():
        print(f"{key}: {value}")
if __name__ == "__main__":
    Dict()
print("\nCode developed by Masino")
