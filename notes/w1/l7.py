# Classes
# __init__() initializes x, y and first parameter is always self

class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def translate(self, deltax, deltay):
        self.x += deltax
        self.y += deltay

    def distance(self):  # distance from origin
        import math
        d = math.sqrt(self.x**2 + self.y**2)
        return d


# other useful constructors
# __str__() converts num to string
# __add__() enables addition of objects
# __mult__(), __ge__() for >=, __lt__ for <, etc


    def __add__(self, p):  # adds self and p
        return Point(self.x + p.x, self.y + p.y)


"""
    we can use (r, theta) instead of (x, y)
    where r is the distance of the point from the origin and
    theta is the angle between the line from origin and the x axis.

    here r = d
    !!!--- SEE NOTES FOR MORE INFORMATION---!!!
"""


class Point2:
    def __init__(self, a=0, b=0):
        import math
        self.r = math.sqrt(a*a + b*b)
        if a == 0:
            self.theta = math.pi/2  # pi/2 = 90 degrees
        else:
            self.theta = math.atan(b/a)  # atan - arctan (inversae of tan)

    def distance2(self):
        return self.r

