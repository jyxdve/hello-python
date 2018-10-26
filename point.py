class Point():
    def __init__(self, x = 0.0, y = 0.0):
       self.x = x
       self.y = y

    def __str__(self):
        return "({}, {})" . format(self.x, self.y)
    
#p = Point()

#print(type(p))


p = Point(3.3, 2.2)
print(p)
q = Point(3.5, 4.6)
print(q)
