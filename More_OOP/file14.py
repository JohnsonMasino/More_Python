#!/usr/bin/python3

def Know_Input():
    """defines the function of the module"""

    name = input("Hi...\nEnter your name here: ")
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    entered = input(f"Hi {name}, enter a single character to determine what it is: ")
    #print(len(entered))

    if len(entered) == 1:
        try:
            if entered in nums:
                print(f"{entered} is a number.")
            elif entered in lower:
                print(f"{name}, you entered a lower case alphabet '{entered}'.")
            elif entered in upper:
                print(f"'{entered}' is an upper case alphabet")
            else:
                print(f"You entered a sign '{entered}'.")
        except Exception as e:
            print(e)
        finally:
            print("Code execution finished")
    else:
        print(f"{name}, enter only one character please.")

if __name__ == "__main__":
    Know_Input()
print("\nCode developed by Masino")
