class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __getitem__(self, item):
        return self.marks[item]

    def __setitem__(self, key, item):
        self.marks[key] = item
    
    def __delitem__(self, key):
        del self.marks[key]

nikita = Student("Nikita", [7, 7, 6, 8, 6, 8])

nikita[2] = 1
del nikita[2]

print(nikita[2])

