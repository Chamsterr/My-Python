class Frange:
    def __init__(self, start=0.0, stop=1.0, step=0.1):
        self.start = start
        self.stop = stop
        self.step = step
        self.value = self.start - self.step

    def __iter__(self):
        self.value = self.start - self.step
        return self

    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration


class Frange2D:
    def __init__(self, start=0.0, stop=1.0, step=0.1, rows = 5):
        self.rows = rows
        self.fr = Frange(start, stop, step)
    
    def __iter__(self):
        self.value = 0
        return self
    
    def __next__(self):
        if self.value < self.rows:
            self.value += 1
            return iter(self.fr)
        else:
            raise StopIteration
    



frange = Frange()
it = iter(frange)

print(next(it))
print(next(it))

fr = Frange2D(rows=5)

for row in fr:
    for x in row:
        print(x)
    print()