from typing import Any


class Counter():
    def __init__(self, counter=0):
        self.counter = counter
    
    def __call__(self, step = 1):
        self.counter += step
        return self.counter

c1 = Counter()
c2 = Counter()

c1()
c1()
c1(-3)

c2(2)
c2(2)
c2(2)

print(c1(), c2(), sep='\n')

#---------------------Замыкание---------------------------
def delete_symbols(chars=" "):
    def delete_from(s: str):
        return s.strip(chars)
    return delete_from

pack1 = delete_symbols(" !?")
pack2 = delete_symbols(None)


print(pack1(" !?1adad2 "))
#---------------------------------------------------------

#-------------------------Класс---------------------------
class delete_symbols:
    def __init__(self, chars):
        self.chars = chars
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        if not isinstance(args[0], str):
            raise TypeError("Аргумент не строка")
        
        return args[0].strip(self.chars)
    
deleter = delete_symbols("12")

print(deleter("2Привет1"))

#---------------------------------------------------------
def log_function_call_1(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with arguments {args}", f"Function {func.__name__} returned: {func(*args)}", sep="\n")
    return wrapper

@log_function_call_1
def add(a, b):
    return a + b

# class log_function_call:
#     """Класс декоратор для логирования"""
#     def __init__(self, func):
#         self.func = func

#     def __call__(self, *args: Any, **kwds: Any) -> Any:
#         print(f"Calling function {self.func.__name__} with arguments {args}", f"Function {self.func.__name__} returned: {self.func(*args)}", sep="\n")

add(12, 11)

diccc  = {}

diccc[(1,2)] = 1

print(diccc)