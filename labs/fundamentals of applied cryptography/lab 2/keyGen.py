from cryptomath import generatePrime, gcd, find_mod_inverse


__all__ = ['keyGen']


def keyGen(keySize: int):
    p = generatePrime(keySize)

    while True:
        e_A = generatePrime(keySize)
        if gcd(e_A, p-1) == 1:
            break

    d_A = find_mod_inverse(e_A, p-1)

    while True:
        e_B = generatePrime(keySize)
        if gcd(e_B, p-1) == 1:
            break

    d_B = find_mod_inverse(e_B, p-1)

    return p, (e_A, d_A), (e_B, d_B)


if __name__ == "__main__":
    print('не использовать как программу. только импортировать!')
