#!/usr/bin/python3
"""
This file uses python to send request to urls
"""

def Getting():
    """defines the get request function"""
    import urllib.request

    try:
        url = 'https://www.google.com'
        resp = urllib.request.Request(url)
        with urllib.request.urlopen(resp) as resp:
            page = resp.read()
        print(resp.code)
        print(type(resp))
        print(resp.peek())
        print(resp.length)
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    Getting()
print("\nCode developed by Masino")
