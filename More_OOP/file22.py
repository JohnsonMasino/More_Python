#!/usr/bin/python3
from datetime import datetime

def Date(Year):
    """defines the date function"""
    Today = datetime.now()
    Today_Year = Today.year
    print(Today_Year - Year)
    return int(Today_Year - Year)

if __name__ == "__main__":
    Date(1999)
print("\nCode developed by Masino")
