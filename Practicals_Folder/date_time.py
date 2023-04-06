#!/usr/bin/python3

import datetime as dt

my_birthday = dt.date(2000, 4, 13)
my_birthday_time = dt.time(6, 45, 13)
print("My birthday date and time is: ", my_birthday, my_birthday_time)
print("Invalid comment: ", dt.timedelta(100))
print("My birthday well arranged is: ", my_birthday.strftime("%A %d %B, %Y"))
#print(my_birthday_time.strftime("%A, %d, %B, %Y"))
print("\nCode developed by Masino")
