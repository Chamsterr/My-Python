class Person:
    def __init__(self, name: str, age: int):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @name.deleter
    def old(self):
        del self.__old


nikita = Person("Nikita", 18)

print(nikita.name)
nikita.name = "Mikita"

print(nikita.name)