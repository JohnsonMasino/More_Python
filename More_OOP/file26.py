#!/usr/bin/python3

def print_name(person):
    """defines the print name function that returns an entered name"""
    try:
        #print(person)
        return person
    except Exception as m:
        print(str(m))
    finally:
        print("Code execution successfull")
if __name__ == "__main__":
    print_name("Johnson")
print("\nCode developed by Masinio")
