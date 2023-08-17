class Point:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point2(Point):
    __slots__ = "v",

    def __init__(self):
        self.z = 15



point = Point(1, 2)
print(point.x, point.y, sep="\n")

point2 = Point2()
print(point2.x, point2.y, point2.z)