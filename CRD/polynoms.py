from ops import Galois
from typing import List



class Polynom:
    def __init__(self, data: List[Galois]):
        self.coef = data

    def __str__(self):
        line = ""
        for i, c in enumerate(self.coef):
            #line += f"{c} "
            line += f"{hex(c.val)[2:].upper()} "
        line += "\n"
        return line

    def message(self) -> str:
        message = ""
        for i in self.coef:
            message += chr(i.val) if i.val != 0 else ""
        return message

    def __add__(self, other):
        l1 = len(self.coef)
        l2 = len(other.coef)
        if l1 > l2:
            other.coef = other.coef + [Galois() for i in range(l1 - l2)]
        else:
            self.coef = self.coef + [Galois() for i in range(l2 - l1)]

        new = []
        for i, j in zip(self.coef, other.coef):
            new.append(i + j)
        return Polynom(new)

    def __mul__(self, other):
        l1 = len(self.coef)
        l2 = len(other.coef)
        new_len = l1 + l2 - 1
        new_coef = [Galois() for i in range(new_len)]
        for i, el1 in enumerate(self.coef):
            for j, el2 in enumerate(other.coef):
                new_coef[i + j] += (el1 * el2)
        return Polynom(new_coef)

    def discard_zeroes(self):
        for i in reversed(self.coef):
            if not i.val:
                self.coef.pop()
            else:
                break
        return self

    def compute(self, n: Galois) -> Galois:
        s = Galois()
        power = Galois(1)
        for i in self.coef:
            s += power * i
            power *= n
        return s

    def divide_by(self, other: 'Polynom') -> ('Polynom', 'Polynom'):
        dividend = self.coef
        divisor = other.coef

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
            dividend = tmp.coef

    def derivative(self) -> 'Polynom':
        if len(self.coef) == 1:
            return Polynom([Galois()])
        coef = []
        for i in range(len(self.coef)):
            if i % 2 == 0:
                coef.append(Galois())
            else:
                coef.append(self.coef[i])
        return Polynom(coef[1:])


    @staticmethod
    def make_poly(data: str) -> 'Polynom':
        coef = []
        for i in data:
            coef.append(Galois(ord(i)))
        return Polynom(coef)
