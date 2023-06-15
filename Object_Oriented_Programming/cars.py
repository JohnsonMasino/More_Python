#!/usr/bin/python3

def Counting():
    """defines the function"""
    print("\nSome cars take off at diferent times and stop at different times.\nRunning this exercise calculates how many cars that were running at the halt time.\nIf a car took off and halted before the halt time, it is not counted.\nAlso if a car took off after the halt time, it is not counted.\nWe only count those cars tha took off before the halt time and stopped after the halt time.")
    startTime = input("\nEnter the start time for each of the cars from the first car to the last car and separate with a space(Enter integers 1 - 100): ")
    endTime = input("Enter the end time for each of the cars from first car to the last car as well and separate with a space(Enter integers 1 - 100): ")
    haltTime = int(input("Enter the general halt time for all the cars: "))
    startTime = startTime.split(" ")
    endTime = endTime.split(" ")
    startTime = [int(i) for i in startTime]
    endTime = [int(i) for i in endTime]
    print("\nThese are the start and end times of each car:")
    count = 1
    num = 1
    for i in startTime:
        """Numbers the start times of each car"""
        print(f"Car {count} took off at {i}")
        count += 1
    print()
    for i in endTime:
        """Numbers the end times of each car"""
        print(f"Car {num} stopped at {i}")
        num += 1
    print(f"The general halt time was {haltTime}.")
    obey = 0
    for i in startTime:
        if i > haltTime:
            obey += 1
        else:
            pass
    for i in endTime:
        if i < haltTime:
            obey += 1
    total = len(endTime)
    rest = total - obey
    print(f"Therefore, it was {obey} cars that were not moving during the halt time.\n{rest} cars disobeyed the traffic rule")

if __name__ == "__main__":
    Counting()
print("\nCode developed by Masino")
