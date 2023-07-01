#!/usr/bin/python3
import urllib.request
import urllib.parse

def Passing():
    """defines the request function"""

    try:
        url = "https://www.google.com/search?q=test"

        headers = {}
        headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
        req = urllib.request.Request(url, headers=headers)
        resp = urllib.request.urlopen(req)
        respData = resp.read()

        saveFile = open('withHeaders.txt', 'w')
        saveFile.write(str(respData))
        saveFile.close()

    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    Passing()
print("\nCode devloped by Masino")
