import os
import sys
import string
from typing import Tuple, List

from termcolor import colored, cprint

import rsa_key_generator as rkg


def get_alhabet_indexes_list_from_text(message: str):
    return [(string.ascii_lowercase+' ').find(x.lower()) for x in message]

def get_text_from_alphabet_indexes(alphabet_indexes: list):
    return ''.join([(string.ascii_lowercase+' ')[x] for x in alphabet_indexes])


def main() -> None:
    print('РСА шифрование')
    if not os.path.exists('rsa_keys.txt'):
        pub_key, priv_key = rkg.generateKey(20)
        n, e = pub_key
        _, d = priv_key
        with open('rsa_keys.txt', 'w') as f:
            f.write('{} {} {}'.format(n, e, d))
    else:
        with open('rsa_keys.txt', 'r') as f:
            n, e, d = list(map(int, f.readlines()[0].split()))

    choose = input('Зашифровать/Расшифровать?[e/d]\n\n> ')
    if choose == 'e':
        message = input('Введите фразу для шифрования\n\n> ')
        ascii_message = get_alhabet_indexes_list_from_text(message)
        ascii_encrypted = [str(pow(x, e, n)) for x in ascii_message]
        with open('encrypted.txt', 'w') as f:
            f.write(' '.join(ascii_encrypted))
    elif choose == 'd':
        choose = input('Из файла или из введенной строки[f/l]?\n\n> ')
        if choose == 'f':
            file_name = input('введите файл с зашифрованным сообщением\n\n> ')
            with open(file_name, 'r') as f:
                encrypted = f.readlines()[0].split()
            decrypted = [pow(int(x), d, n) for x in encrypted]
            ascii_decrypted = get_text_from_alphabet_indexes(decrypted)
            print('Дешифрованная фраза:' + ascii_decrypted)
        elif choose == 'l':
            encrypted = input('Введите через пробел\n\n> ').split()
            decrypted = [pow(int(x), d, n) for x in encrypted]
            ascii_decrypted = get_text_from_alphabet_indexes(decrypted)
            print('Дешифрованная фраза:' + ascii_decrypted)
        else:
            sys.exit()
    else:
        sys.exit('Закрываю программу.')


if __name__ == "__main__":
    if len(sys.argv) == 1:
        main()
    elif all([
        len(sys.argv) > 3,
        sys.argv[1] in ['-e', '-d']
    ]):
        if len(sys.argv[2:]) > 1 and sys.argv[1] == '-d':
            pass
        else:
            pass
    else:
        sys.exit(
            'Программа была прервана, так как не были соблюдены условия:'
            '    Программа должна быть запущена без флагов (python RSA.py)'
            '    Либо c флагами в следующем порядке:'
            '        [-e/-d] keySize:int [phrase:str/encrypted:list[int]]'
        )
