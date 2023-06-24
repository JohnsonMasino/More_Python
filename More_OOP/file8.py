#!/usr/bin/python3

class MyContainer:
    """defines the class of the module"""
    def __init__(self, name, id_no):
        """initialises the parameters of the file"""
        self.name = name
        self.id_no = id_no

    def Container(name, *arg, **kargs):
        """defines the container function of the module"""
        count = 1
        num = 1
        for i in arg:
            print(f"{num}. {i}")
            num += 1
        print()
        for key, value in kargs.items():
            print(f"{count}. {key}: {value}")
            count += 1

if __name__ == "__main__":
    MyContainer.Container("Person", "Johnson Masino", "African", complexion="Fair", net_worth="USD100m", Height="1.9m")
print("\nCode develoepd by Masino")
