#!/usr/bin/python3
"""
This file tried to send request to 'https://www.google.com'
"""

def Google():
    """defines the get function"""
    import urllib.request

    try:
        res = urllib.request.urlopen("https://www.google.com")
        print(res.code)
        data = res.read()
        print(len(data))
        print(data.status_code)
    except Exception as m:
        print(str(m))
    finally:
        print("Code execution finished...")

if __name__ == "__main__":
    Google()
print("\nCode developed by Masino")
