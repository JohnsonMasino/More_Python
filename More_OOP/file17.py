#!/usr/bin/python3

"""
Sends a get request to google.com and reads the source code
"""
def Getting():
    """defines the request funtion of the module"""
    import urllib.request

    gotten = urllib.request.urlopen("https://www.google.com")
    print(gotten.read())

if __name__ == "__main__":
    Getting()
print("\nCode developed by Masino")
