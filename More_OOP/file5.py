#!/usr/bin/python3

def Keyword(name, **keyargs):
    """defines the module of the function"""
    print(f"The name of this container is {name}.\nOne peron discussed as thus:")
    num = 1
    if keyargs is not None:
        for key, value in keyargs.items():
            print(f"{num}. {key}: {value}")
            num += 1
    else:
        print("Nothing to show here...")

if __name__ == "__main__":
    Keyword("Person", Name="Masino", Occupation="Software Engineering", Complexion="Fair", Religion="Christianity", Net_worth="USD69.96m", Hobby="Rapping")
    #Keyword("Person")
print("\nCode developed by Masino")
