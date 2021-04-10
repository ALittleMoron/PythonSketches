from typing import List, Tuple

from termcolor import cprint, colored

from keyGen import keyGen
from cryptomath import find_mod_inverse


def get_ascii_list_from_text(message:str):
    return [code for code in message.encode('ascii')]


def get_text_from_ascii_list(ascii_list: list):
    return ''.join([chr(char) for char in ascii_list])


def shamir() -> None:
    cprint('Реализация протокола Шамира на одной программе.', 'yellow')

    cprint('\nВведите сообщение для отправки другому пользователю.', 'cyan')
    message = input('> ')
    keySize = 16
    
    # Фаза 1: генерация ключей
    p, keys_a, keys_b = keyGen(keySize)
    cprint(f'\nКлючи шифрования пользователя А: {keys_a}\nКлючи шифрования пользователя B: {keys_b}', 'yellow')

    # Фаза 2: алгоритм Шамира
    cprint(f'\nизначальное сообщение: {message}', 'yellow')
    ascii_message = get_ascii_list_from_text(message)
    C1 = [pow(ascii_char, keys_a[0], p) for ascii_char in ascii_message]
    cprint('сообщение на первом шаге алгоритма: {}'.format(''.join(get_text_from_ascii_list(C1))), 'yellow')
    C2 = [pow(C1_char, keys_b[0], p) for C1_char in C1]
    cprint('сообщение на втором шаге алгоритма: {}'.format(''.join(get_text_from_ascii_list(C2))), 'yellow')
    C3 = [pow(C2_char, keys_a[1], p) for C2_char in C2]
    cprint('сообщение на третьем шаге алгоритма: {}'.format(''.join(get_text_from_ascii_list(C3))), 'yellow')
    decrypted_message = [pow(C3_char, keys_b[1], p) for C3_char in C3]
    cprint('дешифрованное сообщение: {}'.format(''.join(get_text_from_ascii_list(decrypted_message))), 'yellow')

if __name__ == "__main__":
    shamir()