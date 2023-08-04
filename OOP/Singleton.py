class Singleton:
    def __new__(cls, *args, **kwargs):
        if getattr(cls, "isinstance", False):
            return cls.isinstance
        cls.isinstance = super().__new__(cls)
        return cls.isinstance


sing = Singleton()
print(id(sing))

sing2 = Singleton()
print(id(sing2))