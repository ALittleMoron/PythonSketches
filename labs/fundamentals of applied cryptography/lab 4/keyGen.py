from random import randrange

from cryptomath import generatePrime, primitive_root, find_mod_inverse


def generate_key(keySize: int) -> tuple[tuple[int, int, int, int], tuple[int, int]]:
    p = generatePrime(keySize)
    e_1 = primitive_root(p)
    d = randrange(3, p)
    e_2 = find_mod_inverse(pow(e_1, d, p), p)

    public_key = (keySize, e_1, e_2, p)
    private_key = (keySize, d)

    return public_key, private_key
