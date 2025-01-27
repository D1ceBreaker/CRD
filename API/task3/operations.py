from typing import List
from ..CRD.polynoms import Polynom, Galois
from ..CRD.main import compute_accuracy, encrypt, environment, decrypt
from random import randint
from ..settings import settings


def plot(a1: int, a2: int, b: int, c: int) -> (List[int], List[float], List[str], List[str], List[str], List[str], int):

    points = a2 + 1 - a1
    d: List[float] = [0 for i in range(points)]
    a: List[int] = [i for i in range(a1, a2 + 1)]
    original: List[str] = ["" for i in range(points * 100)]
    encoded: List[str] = ["" for i in range(points * 100)]
    corrupted: List[str] = ["" for i in range(points * 100)]
    decoded: List[str] = ["" for i in range(points * 100)]
    batch: int = settings.batch

    for i, length in enumerate(a):
        acc = 0
        for j in range(batch):
            poly = generate(length)
            encrypted: Polynom = encrypt(poly, b)
            distorted: Polynom = environment(encrypted, c)
            decrypted: Polynom = decrypt(distorted, b)

            original[i * batch + j] = poly.message()
            encoded[i * batch + j] = encrypted.message()
            corrupted[i * batch + j] = decrypted.message()
            decoded[i * batch + j] = decrypted.message()

            if decrypted.message() != poly.message():
                acc += 1
        acc /= batch
        d[i] = acc
    return a, d, original, encoded, corrupted, decoded, batch


def generate(length: int) -> 'Polynom':
    coefficient = []
    for i in range(length):
        coefficient.append(Galois(randint(1, 255)))
    return Polynom(coefficient)
