import math

class Vector:
    def __init__(self, x, y):
        if not isinstance(x, int or not isinstance(y, int)):
            raise ValueError("should be numbers .")
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector<{self.x}, {self.y}>"

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise ValueError
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise ValueError
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        if not isinstance(scalar, int):
            raise IndexError
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        return self * scalar

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False

    def __getitem__(self, key):
        if key == 'x':
            return self.x
        elif key == 'y':
            return self.y
        else:
            raise KeyError

    def __setitem__(self, key, value):
        if key not in ('x', 'y'):
            raise KeyError
        if not isinstance(value, int):
            raise ValueError("Value should be an integer")
        return(self, key, value)


try:
    v1 = Vector(2, 6)
    v2 = Vector(1, 2)

    print("Vector v1:", v1)
    print("Vector v2:", v2)

    v3 = v1 + v2
    print("v1 + v2:", v3)

    v4 = v1 - v2
    print("v1 - v2:", v4)

    v5 = v1 * 2
    print("v1 * 2:", v5)


except IndexError:
    print("Error")

except ValueError:
    print("Error")

except KeyError:
    print("Error")
