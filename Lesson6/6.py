class Point():

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.list = [self.x, self.y, self.z]

    def sum(self):
        return self.x + self.y + self.z

    def __add__(self, p2):
        return Point(self.x + p2.x, self.y + p2.y, self.z + p2.z)

    def __str__(self):
        return self.list.__str__()



p1 = Point(1, 2, 3)
p2 = Point(-1, 0, 3)

print(p2.sum())

p3 = p1 + p2
print(p3)