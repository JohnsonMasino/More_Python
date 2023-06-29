#!/usr/bin/python3

def FindFile():
    """defines the function of the this module"""
    #from More_Python import More_OOP
    file_name = input("Enter the name of the file you want to search...\nFile path is '~/More_Python/More_OOP': ")
    try:
        if file_name:#in More_OOP:
            print("File is present")
        else:
            print("File absent")
    except Exception as e:
        print(e)
    finally:
        print("Code execution finished")

if __name__ == "__main__":
    FindFile()
print("\nCode developed by Masino")
