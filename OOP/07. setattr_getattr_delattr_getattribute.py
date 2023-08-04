from typing import Any


class Credit_card:
    BANK = "Chamster"

    def __init__(self, number: int, date: str, cvv: int) -> None:
        self.number = number
        self.date = date
        self.__cvv = cvv

    def __getattribute__(self, __name: str) -> Any:
        print(f"__getattribute__ {__name}")
        return object.__getattribute__(self, __name)

    def __setattr__(self, __name: str, __value: Any) -> None:
        print(f"__setattr__: {__name}, {__value}")
        object.__setattr__(self, __name, __value)
    
    def __delattr__(self, __name: str) -> None:
        print("__delattr__")
        object.__delattr__(self, __name)

    def __getattr__(self, item):
        print(f"__getattr__ {item}")


Nikita = Credit_card(4449494994949494, "02.04.2055", 888)

print(Nikita.number)
print(Nikita.balance)
print(Nikita.BANK)

del Nikita.ddd