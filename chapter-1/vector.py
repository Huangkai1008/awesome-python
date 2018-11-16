from math import hypot


class Vector:
    """
    二维向量类
    """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __abs__(self):
        """
        Return the Euclidean distance, sqrt(x*x + y*y).
        :return:
        """
        return hypot(self.x, self.y)

    def __bool__(self):
        return abs(self)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    