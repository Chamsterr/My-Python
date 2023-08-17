class Goods:
    def __init__(self, name, weight, price) -> None:
        super().__init__()
        self.name = name
        self.weight = weight
        self.price = price

    def show_info(self):
        print(f"Инфа из {Goods.__name__}")

    def __str__(self):
        return f"{self.name} - {self.price}$"
    
class MixinClass:
    ID = 0

    def __init__(self):
        self.ID += 1
        self.id = self.ID

    def show_info(self):
        print(f"Тут инфа про что-то ценное {MixinClass.__name__}")

    
class Phone(Goods, MixinClass):
    pass

phone1 = Phone("Пуйфон", 0.200, 5999)
print(MixinClass.ID)
phone2 = Phone("Пуйфон2", 0.140, 10999)

print(phone1, phone1.id)
print(MixinClass.ID)
print(phone2, phone2.id)

print(phone2.show_info())
MixinClass.show_info(phone2)