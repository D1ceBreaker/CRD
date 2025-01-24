from .ops import Galois
from typing import List


class Polynom:
    def __init__(self, data: List[Galois]):
        self.coefficients: List[Galois] = data

    def __str__(self):
        line: str = ""
        for pos, coef in enumerate(self.coefficients):
            # line += f"{c} "
            line += f"{hex(coef.val)[2:].upper()} "
        line += "\n"
        return line

    def message(self) -> str:
        message: str = ""
        for i in self.coefficients:
            message += chr(i.val) if i.val != 0 else ""
        return message

    def __add__(self, other):
        l1: int = len(self.coefficients)
        l2: int = len(other.coefficients)
        if l1 > l2:
            other.coefficients = other.coefficients + [Galois() for i in range(l1 - l2)]
        else:
            self.coefficients = self.coefficients + [Galois() for i in range(l2 - l1)]

        new = []
        for i, j in zip(self.coefficients, other.coefficients):
            new.append(i + j)
        return Polynom(new)

    def __mul__(self, other):
        l1: int = len(self.coefficients)
        l2: int = len(other.coefficients)
        new_len: int = l1 + l2 - 1
        new_coefficients: List[Galois] = [Galois() for _ in range(new_len)]
        for i, el1 in enumerate(self.coefficients):
            for j, el2 in enumerate(other.coefficients):
                new_coefficients[i + j] += (el1 * el2)
        return Polynom(new_coefficients)

    def discard_zeroes(self):
        for i in reversed(self.coefficients):
            if not i.val:
                self.coefficients.pop()
            else:
                break
        return self

    def compute(self, n: Galois) -> Galois:
        s = Galois()
        power = Galois(1)
        for i in self.coefficients:
            s += power * i
            power *= n
        return s

    def divide_by(self, other: 'Polynom') -> ('Polynom', 'Polynom'):
        dividend: List[Galois] = self.coefficients
        divisor: List[Galois] = other.coefficients

        quotient = [Galois() for i in range(len(dividend))]

        main_div = divisor[-1]
        main_power = len(divisor)

        while True:
            power = len(dividend) - main_power
            if power < 0:
                return Polynom(quotient).discard_zeroes(), Polynom(dividend)

            division = dividend[-1] / main_div
            quotient[power] = division

            tmp_coef = [Galois() for _ in range(power + 1)]
            tmp_coef[power] = division

            tmp = Polynom(tmp_coef) * other + Polynom(dividend)
            tmp.discard_zeroes()
            dividend = tmp.coefficients

    def derivative(self) -> 'Polynom':
        if len(self.coefficients) == 1:
            return Polynom([Galois()])
        coef: List[Galois] = []
        for i in range(len(self.coefficients)):
            if i % 2 == 0:
                coef.append(Galois())
            else:
                coef.append(self.coefficients[i])
        return Polynom(coef[1:])

    @staticmethod
    def make_poly(data: str) -> 'Polynom':
        coef: List[Galois] = []
        for i in data:
            coef.append(Galois(ord(i)))
        return Polynom(coef)
