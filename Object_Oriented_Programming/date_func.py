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
        print(f"Todays date is: {today}.\nMeanwhile, Tomorrow's date is: {tomorrow}.")

TimeNow.time()
print("\nCode developed by Masino")
