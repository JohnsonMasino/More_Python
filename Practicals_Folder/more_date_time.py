#!/usr/bin/python3

import datetime as dt
import code_dev as cd
i = cd.statement("\nCode developed by Masino")

required_date = dt.date(2000, 4, 13)
main_thing = dt.timedelta(100)
print(required_date + main_thing)
print(i)
print("My birthday date is: ", required_date)
print("The datatype of this birthday date is: ", type(required_date))
