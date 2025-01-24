from typing import List
from ..CRD.polynoms import Polynom, Galois
from ..CRD.main import compute_accuracy
from random import randint
from ..settings import settings


def plot(a: int, c: int, b1: int, b2: int) -> (List[int], List[float]):
    d: List[float] = []
    b: List[int] = [i for i in range(b1, b2 + 1)]
    for add in b:
        acc = compute_accuracy(generate(a), settings.batch, add, c)
        d.append(acc)
    return b, d


def generate(length: int) -> 'Polynom':
    coefficient = []
    for i in range(length):
        coefficient.append(Galois(randint(1, 255)))
    return Polynom(coefficient)
