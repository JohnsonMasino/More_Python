#!/usr/bin/python3
"""
The request Module
"""

def UrlLib():
    """defines the request function"""
    import urllib.request

    try:
        resp = urllib.request.urlopen("https://www.wikipedia.org")
        print(type(resp))
        print(resp.code)
        print(resp.length)
        print(resp.peek())

        data = resp.read()
        print(type(data))
        #print(data.code)
        print(len(data))

        html = data.decode("UTF-8")
        print(type(html))
        print(html)
        print(resp.peek())
    except Exception as e:
        print(str(e))
    finally:
        print("Code execution finished...")

if __name__ == "__main__":
    UrlLib()
print("\nCode developed by Masino")
