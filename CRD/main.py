from polynoms import Polynom
from ops import Galois


def polynom_generator(n: int) -> Polynom:
    if n <= 0:
        raise AttributeError("n must be > 0")

    array = [Polynom([Galois(2**(i+1)), Galois(1)]) for i in range(n)]
    res = array[0]
    for i in range(1, len(array)):
        res *= array[i]
    return res


def encrypt(message: Polynom, gen: Polynom) -> Polynom:
    tmp = [Galois() for _ in range(len(gen.coef))]
    tmp[-1] = Galois(1)
    tmp_poly = Polynom(tmp)
    # shift polynom by n
    message *= tmp_poly

    q, r = message.divide_by(gen)
    message += r
    #print(message)
    return message

a = Polynom.make_poly("DON'T PANIC")
b = polynom_generator(4)
print("DON'T PANIC: ", a)
print("Polynom gen 4: ", b)
c, d = a.divide_by(b)
print("Rem: ", d)