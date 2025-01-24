from ..CRD.polynoms import Polynom
from ..CRD.main import encrypt, decrypt, environment


def encrypt_decrypt(message: str, n: int, c: int) -> str:

    polynom: Polynom = Polynom.make_poly(message)

    encrypted: Polynom = encrypt(polynom, n)
    distorted: Polynom = environment(encrypted, c)

    decrypted: Polynom = decrypt(distorted, n)

    return decrypted.message()
