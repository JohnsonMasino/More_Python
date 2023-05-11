#!/usr/bin/python3
"""
This class uses the datetime module
"""

class TimeNow:

    def time():
        from datetime import datetime as dt
        from datetime import timedelta as td
        today = dt.now()
        tomorrow = today + td(days=1)
        updated_today = today.strftime("%A %B %d, %y")
        updated_tomorrow = tomorrow.strftime("%A %B %d, %y")
        print(f"{today}\n{tomorrow}")
        print(f"Todays date is: {updated_today}.\nMeanwhile, Tomorrow's date is: {updated_tomorrow}.")

TimeNow.time()
print("\nCode developed by Masino")
