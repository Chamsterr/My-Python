class Phone:
    def __init__(self, size, type=5):
        self.type = type
        self.size = size

phone = Phone(size=5)

print(phone.__dict__)

def some_func():
    """док стринг"""

print(some_func.__doc__)