from fractions import Fraction  # Add the import statement for the Fraction class
import math

class MixedNum:
    def __init__(self, whole, numerator, denominator):
        gcd = math.gcd(numerator, denominator)
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd

        self.whole = whole + numerator // denominator
        self.numerator = self.numerator % self.denominator

    def __repr__(self):
        if self.numerator == 0:
            return str(self.whole)
        return str(self.whole) + ' ' + str(self.numerator) + '/' + str(self.denominator)

    def __add__(self, other):
        fraction1 = Fraction(self.denominator * self.whole + self.numerator, self.denominator)
        fraction2 = Fraction(other.denominator * other.whole + other.numerator, other.denominator)

        fraction3 = fraction1 + fraction2

        return MixedNum(0, fraction3.numerator, fraction3.denominator)

    def __sub__(self, other):
        fraction1 = Fraction(self.denominator * self.whole + self.numerator, self.denominator)
        fraction2 = Fraction(other.denominator * other.whole + other.numerator, other.denominator)

        fraction3 = fraction1 - fraction2

        return MixedNum(0, fraction3.numerator, fraction3.denominator)

    def __mul__(self, other):
        fraction1 = Fraction(self.denominator * self.whole + self.numerator, self.denominator)
        fraction2 = Fraction(other.denominator * other.whole + other.numerator, other.denominator)

        fraction3 = fraction1 * fraction2

        return MixedNum(0, fraction3.numerator, fraction3.denominator)
