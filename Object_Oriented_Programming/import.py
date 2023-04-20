#!/usr/bin/python3
#This function imports a built in module

def Import():
    import sys
    import fibo as fb

    print(fb.fib.__sizeof__)
    print()
    print(sys.path)
    print()
    print(dir(sys))
    print()
    print(sys.float_info)
    print()
    print(sys.hexversion)

Import()    
print("\nCode developed by Masino")
