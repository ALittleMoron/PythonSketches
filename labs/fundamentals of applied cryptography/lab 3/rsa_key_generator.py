import os
import random
import sys
from typing import Tuple

import cryptomath


def generateKey(keySize: int) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    p = cryptomath.generateLargePrime(keySize)
    q = cryptomath.generateLargePrime(keySize)
    n = p * q

    while True:
        e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
        if cryptomath.gcd(e, (p - 1) * (q - 1)) == 1:
            break

    d = cryptomath.find_mod_inverse(e, (p - 1) * (q - 1))

    publicKey = (n, e)
    privateKey = (n, d)
    return (publicKey, privateKey)


def keysFromPQ(p: int, q: int) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    n = p * q

    while True:
        e = random.randrange(p)
        if cryptomath.gcd(e, (p - 1) * (q - 1)) == 1:
            break

    d = cryptomath.find_mod_inverse(e, (p - 1) * (q - 1))

    publicKey = (n, e)
    privateKey = (n, d)
    return (publicKey, privateKey)
