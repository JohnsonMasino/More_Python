#!/usr/bin/python3

def Voting():
    """defines the function of the module"""
    name = input("Enter your name here: ")
    age = int(input(f"Welcome {name}.\nEnter your age here: "))
    try:
        if age < 0:
            print("Invalid input for age")
        elif age >= 0 and age < 18:
            print(f"Sorry {name}. You can not vote currently because you are underaged")
        elif age >= 18 and age < 101:
            print("You can vote...\nContact +234-903-620-6457 to generate your voting pin")
        elif age > 100 and age < 200:
            ans = input("Wow...!\nAre you sure you are this old ?\nType in 'yes' or 'no' to confirm")
            if ans == "yes" or ans == "Yes" or ans == "YES":
                print("Wow okay...!\nContact +234-903-620-6457 to generate your voting pin")
            elif ans == "NO" or ans == "No" or ans == "no":
                print(f"Okay then.\nHave a nice day {name}")
            else:
                print("Unrecognised input")
        elif age >= 200:
            print(f"Sorry but I dont think this age can be real...\nKindly check and try again {name}.")
        else:
            print("Unrecognised Input")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        print("Code execution finished")

if __name__ == "__main__":
    Voting()
print("\nCode developed by Masino")
