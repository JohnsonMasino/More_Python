#!/usr/bin/python3

def People(name):
    """defines the people function"""
    try:
        person = input("Enter name of person here: ")
        print(f"{person} is entered...")
    except Exception as e:
        print(str(e))
    finally:
        print("Code execution finished")
    return name

if __name__ == "__main__":
    People("Masino")
print("\nCode developed by Masino")
