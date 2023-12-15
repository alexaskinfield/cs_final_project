import math

class Fraction:
    def __init__(self, numerator, denominator):
        gcd = math.gcd(numerator, denominator)
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd

    def __repr__(self):
        return str(self.numerator) + '/' + str(self.denominator)

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __sub__(self, other):
        lcm = math.lcm(self.denominator, other.denominator)
        numerator1 = (lcm // self.denominator) * self.numerator
        numerator2 = (lcm // other.denominator) * other.numerator

        return Fraction(numerator1 - numerator2, lcm)
