#!/usr/bin/python3

#This program impoerts the "datetime" package

def DateTime():
    import datetime as dt

    masino_birtheday = dt.date(2000, 4, 13)
    print(dt.time(18, 34, 55))
    print("\nMasino's Birthday is:", masino_birtheday.strftime("%A, %B %d, %Y.\n"))
    print(dir(dt))
    print()
    print(dt.__name__)
    print()
    print(dir(dt.date.today()))

DateTime()
print("\nCode developed by Masino")
