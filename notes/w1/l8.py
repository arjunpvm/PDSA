
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def translate(self, deltax, deltay):
        self.x += deltax
        self.y += deltay

    def distance(self):  # distance from origin
        import math
        d = math.sqrt(self.x*self.x + self.y*self.y)
        return d

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __add__(self, p):  # adds self and p
        return Point(self.x + p.x, self.y + p.y)


p = Point(3, 4)
q = Point(3, 6)

print(p.distance())

# if there is no __str__ or __add__ function
# print(p) will generate error since p is an object and
# it doesnt get changed to string so we use __str__()

print(p)
print(p + q)


class Point2:
    def __init__(self, a=0, b=0):
        import math
        self.r = math.sqrt(a*a + b*b)
        if a == 0:
            self.theta = math.pi/2  # pi/2 = 90 degrees
        else:
            self.theta = math.atan(b/a)  # atan - arctan (inverse of tan)

    def distance(self):
        return self.r


p = Point2(4, 4)
q = Point(3, 6)

print(p.distance())
