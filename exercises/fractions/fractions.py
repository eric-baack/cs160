#!/usr/bin/env python3
"""
Implementation of the class Fraction
"""

## Numerous issues caught by pylint.  Need action:  calling protected (change); using if(type)
## Need to check mypy.
## Passes all tests, black has been used.

def gcd(num_a: int, num_b: int) -> int:
    """
    Greatest Common Denominator of two integers
    Helper function to simplify fractions
    """
    while num_a % num_b:
        num_a, num_b = num_b, num_a % num_b
    return num_b


class Fraction:
    """Class Fraction"""

    def __init__(self, numerator: int, denominator: int) -> None:
        """Initializer"""
        self._numerator = numerator
        self._denominator = denominator
        if not isinstance(self._numerator, int):
            raise TypeError("Numerator must be an integer number")
        if not isinstance(self._denominator, int):
            raise TypeError("Denominator must be an integer number")
        if self._denominator == 0:
            raise TypeError("Denominator must not be zero")

    def get_numerator(self) -> int:
        """Return fraction numerator"""
        return self._numerator

    numerator = property(get_numerator)  ## this was causing error

    def get_denominator(self) -> int:
        """Return fraction denominator"""
        return self._denominator

    denominator = property(get_denominator)  ## this was causing error

    def __str__(self) -> str:
        """Object as a string"""
        common = gcd(
            self._numerator, self._denominator
        )  # obtain greatest common denominator
        new_numer = int(self._numerator / common)
        new_denom = int(self._denominator / common)
        if self._numerator > self._denominator:
            mixed_int = int(new_numer // new_denom)  # obtain first part of mixed number
            mixed_numer = int(new_numer % new_denom)
            frac_str = str(mixed_int) + " " + str(mixed_numer) + "/" + str(new_denom)
        else:
            frac_str = str(new_numer) + "/" + str(new_denom)
        return frac_str

    def __repr__(self) -> str:
        """Object representation"""
        common = gcd(self._numerator, self._denominator)
        new_numer = int(self._numerator / common)
        new_denom = int(self._denominator / common)
        frac_str = f"Fraction({new_numer}, {new_denom})"
        return frac_str

    def __eq__(self, other: object) -> bool:
        """ Fraction equality """
        if isinstance(other, Fraction):
            return (self.numerator * other.denominator) == (
                self.denominator * other.numerator)
        raise TypeError("Can only compare Fractions")

    def __gt__(self, other: object) -> bool:
        """ Test if first fraction is greater than second """
        if isinstance(other, Fraction):
            return (self.numerator * other.denominator) > (
                self.denominator * other.numerator)
        raise TypeError("Can only compare Fractions")

    def __ge__(self, other: object) -> bool:
        """Greater than or equal comparison"""
        if isinstance(other, Fraction):
            return (
                self.numerator / self.denominator >= other.numerator / other.denominator
            )
        raise TypeError("Can only compare Fractions")

    def __add__(self, other: object) -> object:
        if isinstance(other, Fraction):
            return Fraction(
                (
                    self.numerator * other.denominator
                    + self.denominator * other.numerator
                ),
                (self.denominator * other.denominator),
            )
        raise TypeError("Can only add two Fractions")

    def __sub__(self, other: object) -> object:
        """Subtract two fractions"""
        if isinstance(other, Fraction):
            return Fraction(
                (
                    self.numerator * other.denominator
                    - self.denominator * other.numerator
                ),
                (self.denominator * other.denominator),
            )
        raise TypeError("Can only subtract two Fractions")

    def __mul__(self, other: object) -> object:
        """Multiply two fractions"""
        if isinstance(other, Fraction):
            return Fraction(
                (self.numerator * other.numerator),
                (self.denominator * other.denominator),
            )
        raise TypeError("Can only multiply two Fractions")

    def __truediv__(self, other: object) -> object:
        """Divide two fractions"""
        if isinstance(other, Fraction):
            return Fraction(
                (self.numerator * other.denominator),
                (self.denominator * other.numerator),
            )
        raise TypeError("Can only divide two Fractions")


def main():
    """Main function"""
    print("Working with Classes")
    fraction1 = Fraction(10, 4)
    print(f"Fraction 1 is {fraction1}")
    fraction2 = Fraction(10, 12)
    print(f"Fraction 2 is {fraction2}")
    fraction3 = Fraction(3, 4)
    print(f"Fraction 3 is {fraction3}")
    print(f"Its id is {id(fraction3)}")
    fraction4 = Fraction(3, 4)
    print(f"Fraction 4 is {fraction4}")
    print(f"Its id is {id(fraction4)}")

    print("Comparison")
    if fraction3 == fraction4:
        print(f"{fraction3} and {fraction4} are equal!")
    else:
        print(f"{fraction3} and {fraction4} are different!")

    print(f"{fraction1} + {fraction2} = {fraction1 + fraction2}")
    fraction5 = Fraction(3, 2)
    print(repr(fraction5))
    fraction6 = Fraction(10, 3)
    print(str(fraction6))


if __name__ == "__main__":
    main()
