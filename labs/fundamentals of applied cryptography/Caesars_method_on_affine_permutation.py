# imports
import sys
from math import sqrt
from string import ascii_lowercase as alphabet
from string import punctuation


# type hinting
EncryptedString, DecryptedString, JumpledAlphabet = str, str, str


def normalized_alpha_index(index: int) -> int:
    """ Normalize alphabetical shift or index of letter in alphabet.

    Arguments:
        index(int): Shift or index of letter in alphabet.

    Raises:
        TypeError: raise if type of index is not int.
        RecursionError: raise if Recursion stack is overflowed. Set index as default(0)

    Returns:
        index(int): recursively normalized index or shift.
        0: default value. Returns if raising TypeError.
    """
    try:
        return index if index < len(alphabet) else normalized_alpha_index(index - len(alphabet))
    except RecursionError:
        print('Recursion stack was overflowed. index set as default(0)')
        return 0
    except TypeError:
        raise TypeError(f'index must be integer! Got {type(index)}')


def is_formula_correct(a:int, b: int) -> bool:
    """ Validate input formula (at+b). shifts must not be divider of
    alphabet length.

    Arguments:
        a (int): initial shift for jumpling an alphabet.
        b (int): further shift for jumpling an alphabet.

    Returns:
        bool: if 'a' is not divider of alphabet length return True, else False.
    """
    a = normalized_alpha_index(a)
    b = normalized_alpha_index(b)
    if a < 1 or b < 1:
        return False
    dividers = [1]
    al_len = len(alphabet)
    for x in range(2, int(sqrt(al_len))+1):
        if al_len % x == 0:
            dividers.extend([x, al_len/x])
    dividers.extend([al_len])
    dividers = set(dividers)
    return True if (a not in dividers and b not in dividers) else False


def _next_posinion(jumpledAlphabet: list, position: int) -> int:
    """ Find next position in alphabet, that is zero (needs to be switched to letter).

    Args:
        jumpledAlphabet (list): current jumpledAlphabet with zeros to be finded.
        position (int): current position, next state of which should be finded.

    Returns:
        int: next position in alphabet, that is zero.
    """    
    for _ in range(position, len(jumpledAlphabet)):
        position = normalized_alpha_index(position+1)
        if jumpledAlphabet[position] == 0:
            return position
    for _ in range(0, position):
        position = normalized_alpha_index(position+1)
        if jumpledAlphabet[position] == 0:
            return position


def alphabet_from_formula(initialShift: int, furtherShift: int) -> JumpledAlphabet:
    """ Generate jumpled alphabet from 2 shifts.

    Args:
        initialShift (int): shift, that will start jumpling an alphabet.
        furtherShift (int): shift, that will continue jumpling an alphabet.

    Returns:
        JumpledAlphabet: jumpled alphabet from 2 shifts.
    """    
    jumpledAlphabet = [0]* len(alphabet)
    position = initialShift
    for letter in alphabet:
        position = normalized_alpha_index(position)
        if jumpledAlphabet[position] == 0:
            jumpledAlphabet[position] = letter
        else:
            jumpledAlphabet[_next_posinion(jumpledAlphabet, position)] = letter
        position += furtherShift
    return ''.join(jumpledAlphabet)


def encrypting(phrase: str, initialShift: int, furtherShift: int) -> EncryptedString:
    """ Encrypt input phrase with jumpled alphabet.

    Args:
        phrase (str): User's string, that will be enctypted.
        initialShift (int): shift, that will start jumpling an alphabet.
        furtherShift (int): shift, that will continue jumpling an alphabet.

    Returns:
        EncryptedString: enctypted string.
    """    
    encryptedSting = ''
    jumpledAlphabet = alphabet_from_formula(initialShift, furtherShift)

    for letter in phrase:
        if letter in punctuation + ' ':
            encryptedSting += letter
        else:
            if letter.isupper():
                encryptedSting += jumpledAlphabet[alphabet.find(letter.lower())].upper()
            else:
                encryptedSting += jumpledAlphabet[alphabet.find(letter.lower())]
    return encryptedSting


def decrypting(phrase: str, initialShift: int, furtherShift: int) -> DecryptedString:
    """ Decrypt input phrase with jumpled alphabet.

    Args:
        phrase (str): Encrypted string from another encrypt program with same method.
        initialShift (int): shift, that will start jumpling an alphabet.
        furtherShift (int): shift, that will continue jumpling an alphabet.

    Returns:
        DecryptedString: decrypted string.
    """    
    decryptedSting = ''
    jumpledAlphabet = alphabet_from_formula(initialShift, furtherShift)

    for letter in phrase:
        if letter in punctuation + ' ':
            decryptedSting += letter
        else:
            if letter.isupper():
                decryptedSting += alphabet[jumpledAlphabet.find(letter.lower())].upper()
            else:
                decryptedSting += alphabet[jumpledAlphabet.find(letter.lower())]
    return decryptedSting


if __name__ == "__main__":
    args = sys.argv[1:]
    if '-h' in args:
        sys.exit(
'''\npython3 Caesars_method_with_keyword.py [-h] [-d] [-e] phrase initial_shift further_shift

phrase -- str type. User's string, that will be enctypted or decrypted.
initial_shift -- int type. shift, that will start jumpling an alphabet.
further_shift -- str type. shift, that will continue jumpling an alphabet.
''')
    if not args or len(args) != 4:
        sys.exit(f'Sent {len(args)} arguments: {args}. Need 3 arguments: phrase, initial_shift, further_shift; and 1 flag: -d (--decrypt) or -e (--encrypt).')
    if '-e' == args[0]:
        phrase, initial_shift, further_shift = args[1:]
        if is_formula_correct(int(initial_shift), int(further_shift)):
            print(f'Original phrase: "{args[1]}".\nEncrypted phrase: "{encrypting(phrase, int(initial_shift), int(further_shift))}".')
        else:
            print('incorrect formula. "a" or "b" is diveders of alphabet length. Try again with valid values.')
    elif '-d' == args[0]:
        phrase, initial_shift, further_shift = args[1:]
        if is_formula_correct(int(initial_shift), int(further_shift)):
            print(f'Original phrase: "{args[1]}".\nEncrypted phrase: "{decrypting(phrase, int(initial_shift), int(further_shift))}".')
        else:
            print('incorrect formula. "a" or "b" is diveders of alphabet length. Try again with valid values.')
    else:
        sys.exit('No flags: -d or -e; or flag not on the 1st position.')
