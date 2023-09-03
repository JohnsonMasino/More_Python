def Naming():
    """Defines the say name function"""
    name = input("Enter your name here please: ")
    try:
        print(f"You are welcome here {name}.")
    except Exception as e:
        print(str(e))
    finally:
        print("Code execution successful.")
if __name__ == "__main__":
    Naming()