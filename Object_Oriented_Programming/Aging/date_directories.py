#!/usr/bin/python3

"""
This function lists the sub module of the datetime module
"""
def Lists():
    """defines the function"""
    import datetime as dt

    print("Listing from datetime")
    print(dir(dt))
    print("Listing from 'datetime.datetime'")
    print(dir(dt.datetime))

if __name__ == "__main__":
    Lists()

print("\nCode developed by Masino")
