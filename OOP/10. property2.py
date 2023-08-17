class Person:
    def __init__(self, fullname: str, age: int, passport: int, weight: float):
        self.__fullname = fullname
        self.__age = age
        self.__passport = passport
        self.__weight = weight

    @property
    def fullname(self):
        return self.__fullname
    
    @fullname.setter
    def fullname(self, fullname: str):
        self.__fullname = fullname


    @property
    def passport(self):
        return self.__passport
    
    @passport.setter
    def passport(self, passport: int):
        if len(str(passport)) == 10:
            self.__passport = passport
        else:
            raise "фигня давай по новой"

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age: int):
        if 14 < age < 120:
            self.__age = age
        else:
            raise "Сорри возраст не подходит"
    

    @property
    def weight(self):
        return self.__weight
    
    @weight.setter
    def weight(self, weight: int):
        if 20.0 < weight:
            self.__weight = weight
        else:
            raise "Введите реальный вес"