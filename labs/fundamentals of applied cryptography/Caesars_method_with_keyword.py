# imports
import sys
from string import ascii_lowercase as alphabet
from string import punctuation
from random import choice


# type hinting
EncryptedString, DecryptedString, JumpledAlphabet = str, str, str


def alphabet_from_keyword(keyword: str, shift: int) -> JumpledAlphabet:
    shift = normalized_alpha_index(shift)
    jumpledAlphabet = [0 for _ in range(len(alphabet))]
    jumpledAlphabet[shift:len(keyword)+shift] = list(keyword)
    alphabet_without_keyword = sorted(set(alphabet) ^ set(keyword))

    for x in range(len(keyword)+shift, len(alphabet)):
        for y in alphabet_without_keyword:
            if y not in jumpledAlphabet:
                jumpledAlphabet[x] = y
                break
    for x in range(len(keyword)+shift):
        for y in alphabet_without_keyword:
            if y not in jumpledAlphabet:
                jumpledAlphabet[x] = y
                break
    return ''.join(jumpledAlphabet)


def normalized_alpha_index(index: int) -> int:
    """ Normalize alphabetical shift or index of letter in alphabet.

    Arguments:
        index -- int type. Shift or index of letter in alphabet.

    Raises:
        TypeError -- raise if type of index is not int.

    Returns:
        index -- recursively normalized index or shift.
        0 -- default value. Returns if raising TypeError.
    """
    try:
        return index if index < len(alphabet) else normalized_alpha_index(index - len(alphabet))
    except RecursionError:
        print('Recursion stack was overflowed. index set as default(0)')
        return 0
    except TypeError:
        raise TypeError(f'index must be integer! Got {type(index)}')


def encrypting(
        rawString: str,
        shift: int,
        keyword: str) -> EncryptedString:
    """ Encrypting string by Caesar's method with keyword.

    Arguments:
        rawString -- str type. User's string, that will be enctypted.
        shift -- int type. Index of start of alphabet jumpling.
        keyword -- str type. Word from rawString, that will start alphabet
                   from shift to len(keyword).

    Return:
        EncryptedString -- str type. String, that encrypted by Caesar's
                           method with keyword.
    """
    if isinstance(shift, str):
        shift = int(shift)
    encryptedSting = ''
    jumpledAlphabet = alphabet_from_keyword(keyword, shift)

    for letter in rawString:
        if letter in punctuation + ' ':
            encryptedSting += letter
        else:
            if letter.isupper():
                encryptedSting += jumpledAlphabet[alphabet.find(letter.lower())].upper()
            else:
                encryptedSting += jumpledAlphabet[alphabet.find(letter.lower())]
    return encryptedSting


def decrypting(
        encryptedString: EncryptedString,
        shift: int,
        keyword: str) -> DecryptedString:
    """ Encrypting string by Caesar's method with keyword.

    Arguments:
        encryptedString -- EncryptedString type (actually, str type). Encrypted string from
                            another encrypt program.
        shift -- int type. Index of start of alphabet jumpling.
        keyword -- str type. Word (is actually key for decrypt), that will start alphabet
                   from shift to len(keyword).

    Return:
        DecryptedString -- str type. String, that encrypted by Caesar's
                           method with keyword.
    """
    if isinstance(shift, str):
        shift = int(shift)
    decryptedString = ''
    jumpledAlphabet = alphabet_from_keyword(keyword, shift)

    for letter in encryptedString:
        if letter in punctuation + ' ':
            decryptedString += letter
        else:
            if letter.isupper():
                decryptedString += alphabet[jumpledAlphabet.find(letter.lower())].upper()
            else:
                decryptedString += alphabet[jumpledAlphabet.find(letter.lower())]
    return decryptedString



if __name__ == "__main__":
    args = sys.argv[1:]
    if '-h' in args:
        sys.exit(
'''\npython3 Caesars_method_with_keyword.py [-h] [-d] [-e] phrase shift keyword

phrase -- str type. User's string, that will be enctypted.
shift -- int type. Index of start of alphabet jumpling.
keyword -- str type. Word (is actually key for decrypt), that will start alphabet from shift to len(keyword).
''')
    if not args or len(args) != 4:
        sys.exit(f'Sent {len(args)} arguments: {args}. Need 3 arguments: phrase, shift, keyword; and 1 flag: -d (--decrypt) or -e (--encrypt).')
    if '-e' == args[0]:
        phrase, shift, keyword = args[1:]
        print(f'Original phrase: "{args[1]}".\nEncrypted phrase: "{encrypting(phrase, int(shift), keyword)}".')
    elif '-d' == args[0]:
        phrase, shift, keyword = args[1:]
        print(f'Original phrase: "{args[1]}".\nEncrypted phrase: "{decrypting(phrase, int(shift), keyword)}".')
    else:
        sys.exit('No flags: -d or -e; or flag not on the 1st position.')