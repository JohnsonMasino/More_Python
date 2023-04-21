#!/usr/bin/python3

#Importing and Formatting 'datetime' module

def New():
    import datetime as dt

    current = dt.date.today()
    print(current)
    print(current.strftime("%A, %B %d, %Y"))

    my_birthday = dt.date(2000, 4, 13)
    print(my_birthday)

    age = current - my_birthday
    print(age.days)

New()
print("\nCode developed by Masino")
