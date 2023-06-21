#!/usr/bin/python3

def Say_Names(mom, *kids):
    """Defines the module of the function"""
    print(f"The mother is: {mom}")
    num = 1
    for name in kids:
        print(f"Child {num} is: {name}")
        num += 1

if __name__ == "__main__":
    Say_Names("Ijeoma", "Chike", "Adaobi", "Odinaka", "Ndidiamaka", "Ujunwa", "Obinna")
print("\nCode developed by Masino")
