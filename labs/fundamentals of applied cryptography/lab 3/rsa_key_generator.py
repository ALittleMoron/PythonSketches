import os
import random
import sys
from typing import Tuple

import cryptomath_module as cryptoMath


def generateKey(keySize: int) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    p = cryptoMath.generateLargePrime(keySize)
    q = cryptoMath.generateLargePrime(keySize)
    n = p * q

    while True:
        e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
        if cryptoMath.gcd(e, (p - 1) * (q - 1)) == 1:
            break

    d = cryptoMath.find_mod_inverse(e, (p - 1) * (q - 1))

    publicKey = (n, e)
    privateKey = (n, d)
    return (publicKey, privateKey)


def makeKeyFiles(name: str, keySize: int) -> None:
    publicKey, privateKey = generateKey(keySize)

    with open(f"{name}_pubkey.txt", "w") as out_file:
        out_file.write(f"{keySize},{publicKey[0]},{publicKey[1]}")

    with open(f"{name}_privkey.txt", "w") as out_file:
        out_file.write(f"{keySize},{privateKey[0]},{privateKey[1]}")