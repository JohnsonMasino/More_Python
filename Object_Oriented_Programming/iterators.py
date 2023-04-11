#!/usr/bin/python3

"""
This peice of code utilises iterators
"""
def iterate():
    print("First for loop:")
    for element in [1, 2, 3]:
        print(element)
    print("\nSecond For loop:")    
    for more in (7, 8, 9):
        print(more)
    print("\nThird for loop:")    
    for one in {"one":1, "two":2, "three":3}:
        print(one)
    print("\nFourth for loop:")    
    for ch in '123':
        print(ch)
    print("\nFifth for loop:")    
    for line in open("iterators.py"):
        print(line, end='')
iterate()
print('\nCode developed by Masino')
