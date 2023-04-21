#!/usr/bin/python3

#This program tries to modify a list

def Lists():
    a = [4, 6, 8, 2]
    b = a
    print("a =", a)
    print("b = a")
    print("a and b point to same object", "\na =", b, "\nb =", a)
    print("\nchanges to b affects a")
    print("b[2] = 9")
    b[2] = 9
    print('a =', a)

    print("\nTo make a copy of a and store in c, do this:\nc = a[:]")
    print("\nNow print c")
    c = a[:]
    print(c)
    print("\nChanges to c will not affect a now:\nc[0] = 3")
    print("\nNow print a and c and see the difference in the first element:")
    c[0] = 3
    print(f"a = {a}\nc = {c}")

Lists()
print("\nCode developed by Masino")
