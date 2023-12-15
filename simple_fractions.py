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

    def __add__(self, other):
        lcm = math.lcm(self.denominator, other.denominator)
        numerator1 = (lcm // self.denominator) * self.numerator
        numerator2 = (lcm // other.denominator) * other.numerator

        return Fraction(numerator1 + numerator2, lcm)

    def __mul__(self, other):
        # Multiplying the numerators and denominators
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator

        # Calculating the greatest common divisor
        gcd = math.gcd(numerator, denominator)

        return Fraction(numerator // gcd, denominator // gcd)

    # Example usage:
    fraction1 = Fraction(3, 4)
    fraction2 = Fraction(2, 5)

    result = fraction1 * fraction2
    print(result)

 def __truediv__(self, other):
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator

        # Calculating the greatest common divisor
        gcd = math.gcd(numerator, denominator)

        return Fraction(numerator // gcd, denominator // gcd)

# Example usage:
fraction1 = Fraction(3, 4)
fraction2 = Fraction(2, 5)

result = fraction1 / fraction2
print(result)







