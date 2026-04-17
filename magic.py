class Point: 
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"[{self.x} , {self.y}]"
    def __gt__(self, other):
        return self.x > other.x
    def __getitem__(self, key):
        if key == 'x':
            return self.x
        if key == 'y':
            return self.y
        return 'None'

point1 = Point(5, 4)
point2 = Point(1, 70)
print(point1)

print (point1 > point2)

print(point2['x'])
print(point2['x'])
print(point2['yuu'])