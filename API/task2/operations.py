from typing import List

from ..CRD.main import encrypt, environment, decrypt
from ..CRD.polynoms import Polynom, Galois
from random import randint
from ..settings import settings


def plot(a: int, c: int, b1: int, b2: int) -> (List[int], List[float], List[str], List[str], List[str], List[str], int):
    points = b2 + 1 - b1
    d: List[float] = [0 for i in range(points)]
    b: List[int] = [i for i in range(b1, b2 + 1)]
    original: List[str] = ["" for i in range(points * 100)]
    encoded: List[str] = ["" for i in range(points * 100)]
    corrupted: List[str] = ["" for i in range(points * 100)]
    decoded: List[str] = ["" for i in range(points * 100)]
    batch: int = settings.batch
    for i, add in enumerate(b):
        acc = 0
        for j in range(batch):
            poly = generate(a)
            encrypted: Polynom = encrypt(poly, add)
            distorted: Polynom = environment(encrypted, c)
            decrypted: Polynom = decrypt(distorted, add)

            original[i * batch + j] = poly.message()
            encoded[i * batch + j] = encrypted.message()
            corrupted[i * batch + j] = decrypted.message()
            decoded[i * batch + j] = decrypted.message()

            if decrypted.message() != poly.message():
                acc += 1
        acc /= batch
        d[i] = acc
    return b, d, original, encoded, corrupted, decoded, batch


def generate(length: int) -> 'Polynom':
    coefficient = []
    for i in range(length):
        coefficient.append(Galois(randint(1, 255)))
    return Polynom(coefficient)



