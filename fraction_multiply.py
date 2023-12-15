import math

class Fraction:
    def __init__(self, numerator, denominator):
        gcd = math.gcd(numerator, denominator)
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd

    def __repr__(self):
        return f"{self.numerator}/{self.denominator}"

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

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
