class Python:
    info = "1.0"

    @classmethod
    def show_info(cls):
        print(cls.info)

    @staticmethod
    def show_static_info():
        print("I'am programming language")
        
    @staticmethod
    def prosto_show_info():
        print("Просто информация")

class Python3_1(Python):
    info = "3.1"


test = Python3_1()

test.show_info()

Python3_1.show_static_info()
test.show_static_info()

Python3_1.prosto_show_info()

test.prosto_show_info()
