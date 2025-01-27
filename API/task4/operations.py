from typing import List

from ..CRD.polynoms import Polynom, Galois
from ..CRD.main import encrypt, decrypt, environment
from random import randint



def isDecryptable(a: int, b: int, c: int) -> (bool, List[str], List[str], List[str], List[str]):

    polynom: Polynom = generate(a)

    encrypted: Polynom = encrypt(polynom, b)
    distorted: Polynom = environment(encrypted, c)

    decrypted: Polynom = decrypt(distorted, b)

    return decrypted.message() == polynom.message(), [polynom.message()], [encrypted.message()], [distorted.message()], [decrypted.message()]


def generate(length: int) -> 'Polynom':
    coefficient = []
    for i in range(length):
        coefficient.append(Galois(randint(1, 255)))
    return Polynom(coefficient)