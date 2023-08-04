class Dog:
    def __new__(cls, *args, **kwargs):
        print("calling new")
        return super().__new__(cls)

    def __init__(self):
        print("calling init")


batty = Dog()
print(batty.__dict__)