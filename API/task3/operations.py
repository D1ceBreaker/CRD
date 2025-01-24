from typing import List
from ..CRD.polynoms import Polynom, Galois
from ..CRD.main import compute_accuracy
from random import randint
from ..settings import settings


def plot(a1: int, a2: int, b: int, c: int) -> (List[int], List[float]):
    d: List[float] = []
    a: List[int] = [i for i in range(a1, a2 + 1)]

    for length in a:
        acc = compute_accuracy(generate(length), settings.batch, b, c)
        d.append(acc)
    return a, d


def generate(length: int) -> 'Polynom':
    coefficient = []
    for i in range(length):
        coefficient.append(Galois(randint(1, 255)))
    return Polynom(coefficient)
