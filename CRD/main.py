from typing import List

from polynoms import Polynom
from ops import Galois


def polynom_generator(n: int) -> Polynom:
    if n <= 0:
        raise AttributeError("n must be > 0")

    array = [Polynom([Galois(2).power(i + 1), Galois(1)]) for i in range(n)]
    res = array[0]
    for i in range(1, len(array)):
        res *= array[i]
    return res


def encrypt(message: Polynom, gen: Polynom) -> Polynom:
    tmp = [Galois() for _ in range(len(gen.coefficients))]
    tmp[-1] = Galois(1)
    tmp_poly = Polynom(tmp)
    message *= tmp_poly

    q, r = message.divide_by(gen)
    message += r
    return message


def syndrom_polynom(enc: Polynom, n: int):
    array = [enc.compute(Galois(2).power(i + 1)) for i in range(n)]

    return Polynom(array)


def locator_polynom(errors: List[int]) -> Polynom:
    array = [Polynom([Galois(1), Galois(2).power(i)]) for i in errors]
    res = array[0]
    for i in range(1, len(array)):
        res *= array[i]
    return res


def error_polynom(syndrome: Polynom, locator: Polynom, n: int):
    res = syndrome * locator
    return Polynom(res.coefficients[:n])


def magnitudes(syndrome: Polynom, errors: List[int], n: int):
    locator = locator_polynom(errors)
    err = error_polynom(syndrome, locator, n)
    loc_der = locator.derivative()

    mag = [Galois() for i in range(max(errors) + 1)]

    for i in errors:
        xi = Galois(1) / Galois(2).power(i)
        w = err.compute(xi)
        l = loc_der.compute(xi)
        mag[i] = w / l
    return Polynom(mag)


def find_errors(syndrome: Polynom, n: int):
    locator = Polynom([Galois(1)])
    prev_locator = Polynom([Galois(1)])
    shift = 0

    for i in range(n):
        k = i + shift
        delta = syndrome.coefficients[k]

        for j in range(1, len(locator.coefficients)):
            delta += locator.coefficients[j] * syndrome.coefficients[k - j]
        prev_locator *= Polynom([Galois(0), Galois(1)])

        if delta.val != 0:
            if len(prev_locator.coefficients) > len(locator.coefficients):
                new_locator = prev_locator * Polynom([delta])
                prev_locator = locator * Polynom([Galois(1) / delta])
                locator = new_locator

            locator += prev_locator * Polynom([delta])
    return locator


def pos_errors(locator: Polynom) -> List[int]:
    array = []
    for i in range(256):
        if locator.compute(Galois(i)).val == 0:
            a = Galois(1) / Galois(i)
            d = a.log()
            array.append(d.val)
    return array


def decrypt(message: Polynom, n: int):
    syndrome = syndrom_polynom(message, n)
    location = find_errors(syndrome, n)
    errors = pos_errors(location)
    errors.sort()
    mag = magnitudes(syndrome, errors, n)
    message += mag
    return Polynom(message.coefficients[n:])


a = Polynom.make_poly("DON'T PANIC")
b = polynom_generator(4)
e = encrypt(a, b)
e.coefficients[6] = Galois(ord("A"))
e.coefficients[13] = Galois(ord("A"))

print(decrypt(e, 4).message())
