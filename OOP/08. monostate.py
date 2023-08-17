class Thread:
    sharred_attr = {
        'number_of_orders': 0
    }

    def __init__(self):
        self.__dict__ = Thread.sharred_attr
    

Thread.sharred_attr["number_of_orders"] = 5

th = Thread()
print(th.__dict__)

Thread.sharred_attr["number_of_orders"] = 55

th2 = Thread()
print(th2.__dict__)
