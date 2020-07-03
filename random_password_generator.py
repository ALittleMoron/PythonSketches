from random import choice
from string import (ascii_letters, ascii_lowercase,
                    ascii_uppercase, digits, punctuation)
import pyperclip
import sys


# более наглядное представление возвращаемого значения
copied_password = str


def rnd_password_generator(length:int) -> copied_password:
    """функция генерирует сложный случайный пароль, состоящий из
       спец. символов, цифр, латиницы в верхнем и нижнем регистре

       аргументы фунеции:
       length -- длина генерируемого пароля

       возвращаемое значение:
       copied_password -- сгенерированный и скопированный в буфер обмена пароль
    """
    all_chars = ascii_letters + ascii_lowercase + ascii_uppercase +\
                digits + punctuation

    password = ''.join(choice(all_chars) for _ in range(length))
    pyperclip.copy(password)

    return password


if __name__ == "__main__":
    a = rnd_password_generator(25)
    print(a)
    input("Press any key (not shutdown button) to exit... ")
