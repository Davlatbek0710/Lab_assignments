def Euclidian_alg(a, b):
    if b == 0:
        return a
    elif a > b:
        return Euclidian_alg(b, a % b)
    elif b > a:
        return Euclidian_alg(b, a)


class Fraction:
    def __init__(self, numerator, denominator):
        if numerator == denominator:
            self.top = numerator // denominator
            self.bottom = denominator // numerator
        else:
            gcd = Euclidian_alg(numerator, denominator)
            self.top = numerator // gcd
            self.bottom = denominator // gcd

    def __str__(self):
        if self.bottom == 1:
            return str(self.top)
        else:
            return str(self.top) + "/" + str(self.bottom)

    def __add__(self, other):  # addition of fraction
        if self.bottom != other.bottom:
            self.new_top = self.top * other.top + other.bottom * self.top
            self.new_bottom = self.bottom * other.bottom
            return Fraction(self.new_top, self.new_bottom)
        elif self.bottom == other.bottom:
            self.new_top = self.top + other.top
            return Fraction(self.new_top, other.bottom)

    def __sub__(self, other):  # subtraction of fractions
        if self.bottom == other.bottom:
            self.new_top = self.top - other.top
            return Fraction(self.new_top, other.bottom)
        else:
            self.new_top = other.bottom * self.top - self.bottom * other.top
            self.new_bottom = self.bottom * other.bottom
            return Fraction(self.new_top, self.new_bottom)

    def __mul__(self, other):  # multiplication of fractions
        self.new_top = self.top * other.top
        self.new_bottom = self.bottom * other.bottom
        return Fraction(self.new_top, self.new_bottom)

    def __divmod__(self, other):  # division of fractions
        self.new_top = self.top * other.bottom
        self.new_bottom = self.bottom * other.top
        return Fraction(self.new_top, self.new_bottom)

    # Algorithm for float dividing
    def __floordiv__(self, other):
        self.new_top = self.top * other.bottom
        self.new_bottom = self.bottom * other.top
        return Fraction(self.new_top, self.new_bottom)


# These print operations shows the different operations with fractions
print(Fraction(5, 3).__add__(Fraction(1, 3)))  # addition
print(Fraction(5, 3).__sub__(Fraction(1, 3)))  # subtraction
print(Fraction(22, 11).__mul__(Fraction(1, 2)))  # multiplication
print(Fraction(22, 3).__divmod__(Fraction(22, 2)))  # division
# You can write is as shown below
print(Fraction(5, 3) + (Fraction(1, 3)))
print(Fraction(5, 3) - (Fraction(1, 3)))
print(Fraction(5, 3) * (Fraction(1, 3)))
print(Fraction(22, 3) // (Fraction(22, 2)))
