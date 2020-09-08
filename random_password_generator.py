from random import choice
from string import (ascii_letters, ascii_lowercase,
                    ascii_uppercase, digits, punctuation)
import sys
import pyperclip


# более наглядное представление возвращаемого значения
CopiedPassword = str


def rnd_password_generator(length: int, char_set: str) -> CopiedPassword:
    """функция генерирует сложный случайный пароль, состоящий из
       спец. символов, цифр, латиницы в верхнем и нижнем регистре

       аргументы фунеции:
       length -- длина генерируемого пароля
       char_set -- набор символов в виде строки

       возвращаемое значение:
       copied_password -- сгенерированный и скопированный в буфер обмена пароль
    """
    password = ''.join(choice(char_set) for _ in range(length))
    pyperclip.copy(password)

    return password


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if len(sys.argv) == 2:
            chars = ascii_letters + ascii_lowercase + ascii_uppercase +\
                    digits
        elif len(sys.argv) == 3 and sys.argv[2] in ('1', 'True', 'yes', 'y',
                                                    'Y'):
            chars = ascii_letters + ascii_lowercase + ascii_uppercase +\
                    digits + punctuation
        elif len(sys.argv) == 3 and sys.argv[2] in ('0', 'False', 'no', 'n',
                                                    'N'):
            chars = ascii_letters + ascii_lowercase + ascii_uppercase +\
                    digits
        else:
            raise Exception('oops!')
        print(rnd_password_generator(int(sys.argv[1]), chars))

    else:
        print('use arguments to execute code (args: length, char_set)')
    input("Press any key (not shutdown button) to exit... ")
