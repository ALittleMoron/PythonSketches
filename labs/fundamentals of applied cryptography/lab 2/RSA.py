import os
import sys
from typing import Tuple, List

from termcolor import colored, cprint

import rsa_key_generator as rkg


DEFAULT_BLOCK_SIZE = 128
BYTE_SIZE = 256


def get_blocks_from_text(
        message: str, 
        block_size: int = DEFAULT_BLOCK_SIZE) -> List[int]:
    message_bytes = message.encode("ascii")

    block_ints = []
    for block_start in range(0, len(message_bytes), block_size):
        block_int = 0
        for i in range(block_start, min(block_start + block_size, len(message_bytes))):
            block_int += message_bytes[i] * (BYTE_SIZE ** (i % block_size))
        block_ints.append(block_int)
    return block_ints


def get_text_from_blocks(
        block_ints: List[int], 
        message_length: int, 
        block_size: int = DEFAULT_BLOCK_SIZE) -> str:
    message: list[str] = []
    for block_int in block_ints:
        block_message: list[str] = []
        for i in range(block_size - 1, -1, -1):
            if len(message) + i < message_length:
                ascii_number = block_int // (BYTE_SIZE ** i)
                block_int = block_int % (BYTE_SIZE ** i)
                block_message.insert(0, chr(ascii_number))
        message.extend(block_message)
    return "".join(message)


def encrypt_message(
        message: str, 
        key: Tuple[int, int], 
        blockSize: int = DEFAULT_BLOCK_SIZE) -> List[int]:
    encrypted_blocks = []
    n, e = key

    for block in get_blocks_from_text(message, blockSize):
        encrypted_blocks.append(pow(block, e, n))
    return encrypted_blocks


def decrypt_message(
        encrypted_blocks: List[int],
        message_length: int,
        key: Tuple[int, int],
        block_size: int = DEFAULT_BLOCK_SIZE) -> str:
    decrypted_blocks = []
    n, d = key
    for block in encrypted_blocks:
        decrypted_blocks.append(pow(block, d, n))
    return get_text_from_blocks(decrypted_blocks, message_length, block_size)


def read_key_file(key_filename: str) -> Tuple[int, int, int]:
    with open(key_filename) as fo:
        content = fo.read()
    key_size, n, EorD = content.split(",")
    return (int(key_size), int(n), int(EorD))


def encrypt_and_write_to_file(
        message_filename: str,
        key_filename: str,
        message: str,
        block_size: int = DEFAULT_BLOCK_SIZE) -> str:
    key_size, n, e = read_key_file(key_filename)
    if key_size < block_size * 8:
        sys.exit(
            "ERROR: Block size is %s bits and key size is %s bits. The RSA cipher "
            "requires the block size to be equal to or greater than the key size. "
            "Either decrease the block size or use different keys."
            % (block_size * 8, key_size)
        )

    encrypted_blocks = [str(i) for i in encrypt_message(message, (n, e), block_size)]

    encrypted_content = ",".join(encrypted_blocks)
    encrypted_content = f"{len(message)}_{block_size}_{encrypted_content}"
    with open(message_filename, "w") as fo:
        fo.write(encrypted_content)
    return encrypted_content


def read_from_file_and_decrypt(message_filename: str, key_filename: str) -> str:
    err_message = [
        "ОШИБКА: Размер блока = {} бит и размер ключа = {} бит. RSA шифр ",
        "требует, чтобы размер блока был больше или равен размеру ключа. ",
        "Правильно ли вы указали файл с ключами и файл с зашифрованным сообщением?",
    ]
    key_size, n, d = read_key_file(key_filename)
    with open(message_filename) as fo:
        content = fo.read()
    message_length_str, block_size_str, encrypted_message = content.split("_")
    message_length = int(message_length_str)
    block_size = int(block_size_str)

    if key_size < block_size * 8:
        sys.exit(colored(''.join(err_message).format(block_size * 8, key_size), 'red'))

    encrypted_blocks = []
    for block in encrypted_message.split(","):
        encrypted_blocks.append(int(block))

    return decrypt_message(encrypted_blocks, message_length, (n, d), block_size)


def main() -> None:
    filename = "encrypted_file.txt"
    response = input(colored(r"Зашифровать/расшифровать? [e/d]: ", 'cyan'))

    cprint("\nПроверка на то, что у вас есть ключи для шифрования. ", 'yellow')
    keyfilename = input(colored("Введите первую часть файла до нижнего подчеркивания (по умолчанию, \"rsa\"): ", 'cyan'))

    if not os.path.exists(f"{keyfilename}_pubkey.txt") or not os.path.exists(f"{keyfilename}_privkey.txt"):
        rkg.makeKeyFiles(keyfilename, 1024)

    if response.lower().startswith("e"):
        message = input(colored("\nВведите сообщение для зашифровки: ", 'cyan'))
        pubkey_filename = "rsa_pubkey.txt"
        cprint(f"\nЗашифровка и запись результата в {filename}...", 'yellow')
        encryptedText = encrypt_and_write_to_file(filename, pubkey_filename, message)

        cprint("\nЗашифрованный текст:", 'cyan')
        cprint(encryptedText, 'yellow')
    elif response.lower().startswith("d"):
        privkey_filename = "rsa_privkey.txt"
        cprint(f"\nЧтение из файла {filename} и дешифровка...", 'yellow')
        decrypted_text = read_from_file_and_decrypt(filename, privkey_filename)
        cprint("Запись расшифрованного сообщения в rsa_decryption.txt...", 'yellow')
        with open("rsa_decryption.txt", "w") as dec:
            dec.write(decrypted_text)

        cprint("\nРасшифрованное сообщение:", 'cyan')
        cprint(decrypted_text, 'yellow')


if __name__ == "__main__":
    main()