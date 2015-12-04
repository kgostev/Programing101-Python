from copy import deepcopy


class Fraction:

    def gcd(self, numerator, denominator):
        while denominator:
            numerator, denominator = denominator, numerator % denominator
        return numerator

    def _divise_fraction(self, f):
        while self.gcd(f.__numerator, f.__denominator) > 1:
            div = self.gcd(f.__numerator, f.__denominator)
            f.__numerator //= div
            f.__denominator //= div
        return f

    def __init__(self, numerator, denominator):
        self.__numerator = numerator
        self.__denominator = denominator

    def __str__(self):
        if self.__denominator == 1:
            return str(self.__numerator)
        else:
            return "{} / {}".format(self.__numerator, self.__denominator)

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        f = Fraction(self.__numerator * other.__denominator + other.__numerator *
                     self.__denominator, self.__denominator * other.__denominator)
        return self._divise_fraction(f)

    def __sub__(self, other):
        f = Fraction(self.__numerator * other.__denominator -
                     other.__numerator * self.__denominator,
                     self.__denominator * other.__denominator)
        return self._divise_fraction(f)

    def __mul__(self, other):
        f = Fraction(self.__numerator * other.__numerator,
                     self.__denominator * other.__denominator)
        return self._divise_fraction(f)

    def __eq__(self, other):
        f1 = deepcopy(self)
        f2 = deepcopy(other)
        f1 = self._divise_fraction(f1)
        f2 = self._divise_fraction(f2)
        return f1.__denominator == f2.__denominator and f1.__numerator == f2.__numerator

    def __hash__(self):
        return hash(self.__numerator + self.__denominator)


f1 = Fraction(1, 2)
f2 = Fraction(2, 4)

print(f1)
print(f2)
print('\'+\'', f1 + f2)
print('\'*\'', f1 * f2)
print('\'-\'', f1 - f2)
print('\'==\'', f1 == f2)
