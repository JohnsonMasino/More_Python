#!/usr/bin/python3

def Printing(name):
    """Defines the printing function"""
    try:
        nm = input("Enter your name here please: ")
        print(f"{nm} is registred.\nThank you!")
    except Exception as e:
        print(str(e))
    finally:
        print("Code execution finished")

if __name__ == "__main__":
    Printing("Masino")
print("\nCode developed by Masino")
