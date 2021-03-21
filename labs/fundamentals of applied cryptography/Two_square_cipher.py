from string import ascii_lowercase
from typing import List, Tuple
from random import shuffle
from copy import deepcopy
import pprint


class DecryptError(Exception):
    pass


class Cipher():
    """ Class of two square cipher, that can encrypt
    and decrypt input string with jumpled alhabet.
    
    Cases of use:
    >>> a = Cipher()
    >>> print(a.encrypt('Your string'))
    'Gvaz ugstlz'

    >>> a = Cipher(two_sqoares_list=your_two_alphabets)
    >>> print(a.decrypt('Gvaz ugstlz'))
    'Your string'

    """    
    def __init__(self, two_squares_list: list=None):
        if two_squares_list == None:
            self.A = Cipher._jumpled_random_square_alphabet()
            self.B = Cipher._jumpled_random_square_alphabet()
            self.two_squares_list = Cipher.two_squares(self.A, self.B)
            self.to_decrypt = False
        else:
            self.two_squares_list = two_squares_list
            self.A, self.B = Cipher.split_two_square_list(self.two_squares_list)
            self.to_decrypt = True


    @staticmethod
    def split_two_square_list(combined_list:list) -> Tuple[List[List[str]]]:
        """ Split list of combined two square jumpled alphabet.

        Args:
            combined_list (list): combined square alphabet.

        Returns:
            (A, B) (tuple): tuple of splited lists
        """        
        A = [combined_list[i][:5] for i in range(5)]
        B = [combined_list[i][5:] for i in range(5)]
        return A, B


    @staticmethod
    def _jumpled_random_square_alphabet() -> List[List[int]]:
        """ jumple alphabet from random shuffled positions of chars.

        Returns:
            list: jumpled alphabet as 5x5 matrix.
        """        
        positions = [(x, y) for x in range(5) for y in range(5)]
        shuffle(positions) # make it be random for inserte chars
        square = [[0 for _ in range(5)] for _ in range(5)]
        ascii_letters = ascii_lowercase.replace('i', '') # i = j in square

        count = 0
        for x, y in positions:
            if count > len(ascii_lowercase):
                break
            if square[x][y] == 0:
                if ascii_letters[count] == 'j':
                    square[x][y] = ascii_letters[count] + 'i'
                else:
                    square[x][y] = ascii_letters[count]
                count += 1

        return square


    @staticmethod
    def two_squares(A: list, B: list) -> list:
        """combines two alphabets(matrix) into one.

        Returns:
            list: combined matrix from two alphabets.
        """
        return [A[i]+B[i] for i in range(len(A))]


    def _find_char_pos(self, alphabet:list, char: str) -> list:
        """ Method, that find char position in matrix jumpled alphabet.

        Args:
            alphabet (List[List[str]]): matrix jumpled alphabet.
            char (str): letter of english alphabet.

        Returns:
            list: position of passed char. Example: [3, 0] or [2, 4].
        """        
        if char in ('i', 'j'):
            char = 'ji'
        for e_1, row in enumerate(alphabet):
            for e_2, letter in enumerate(row):
                if letter == char:
                    return [e_1, e_2]
        return [-1, -1]


    def oposide_positions_of_chars(self, bigram: str) -> list:
        """ Find positions of 2 bigram oposide chars.

        Args:
            bigram (str): two letters in 1 string, like 'ab'.

        Returns:
            list of tuples:  list of left and right positions like [(x1,y1), (x2,y2)]
        """        
        left, right = list(bigram)
        l_pos = self._find_char_pos(self.A, left)
        r_pos = self._find_char_pos(self.B, right)
        # if chars are not on the same line
        if l_pos[0] < r_pos[0] or l_pos[0] > r_pos[0]:
            l_pos[0], r_pos[0] = r_pos[0], l_pos[0]
            r_pos[1] += 5
        # if chars are on the same line
        elif l_pos[0] == r_pos[0]:
            l_pos[1], r_pos[1] = r_pos[1]+6, l_pos[1]-1
        else:
            raise IndexError("Can't find positions.")
        if l_pos[1] >= 10:
            l_pos[1] -= 10
        if r_pos[1] >= 10:
            r_pos[1] -= 10
        return l_pos, r_pos 


    def _values_from_oposide(self, positions: List[Tuple[str]]) -> List[str]:
        return [self.two_squares_list[x][y] for x, y in positions]


    @staticmethod
    def make_bigram_from_string(string: str) -> List[str]:
        """ Take string and make list of char pairs(bigram) without spaces.

        Args:
            string (str): string of letters without punctuation. Adding 'z' char, if string lenght
                of string is odd.

        Returns:
            List[str]: lisft of bigrams. Example: ['th', 'is', 'my', 'st', 'ri', 'ng']
        """        
        bigram = []
        string = string.replace(' ', '')
        prev_pos = 0
        
        if len(string) % 2 == 1:
            string += 'z'
        
        try:
            for next_pos in range(2, len(string)+2, 2):
                bigram.append(string[prev_pos:next_pos])
                prev_pos = next_pos
        except IndexError as e:
            print(e)
            exit()
        
        return bigram


    def encrypt(self, input_str: str) -> str:
        """ Main method. Encrypt input string by two square cipher.

        Args:
            input_str (str): string of letters without punctuation. Adding 'z' char, if string lenght
                of string is odd.

        Returns:
            str: encrypted string.
        """        
        bigram = Cipher.make_bigram_from_string(input_str)
        encrypt_string = ''

        for pair in bigram:
            oposide = self.oposide_positions_of_chars(pair)
            encrypt_string += ''.join(self._values_from_oposide(oposide))

        return encrypt_string


    def decrypt(self, input_str: str) -> str:
        """ Main method. Decrypt input string by two square cipher.

        Args:
            input_str (str): string of encrypted letters without punctuation. Adding 'z' char, if string lenght
                of string is odd.

        Raises:
            DecryptError: raise if Cipher class were init by encrypt settings. (for decryption init you need to 
                create an instance of the class with the passed argument 'two_square_list').

        Returns:
            str: decrypted string.
        """        
        if self.to_decrypt:
            bigram = Cipher.make_bigram_from_string(input_str)
            decrypt_string = ''

            for pair in bigram:
                oposide = self.oposide_positions_of_chars(pair)
                decrypt_string += ''.join(self._values_from_oposide(oposide))

            return decrypt_string

        else:
            raise DecryptError("Can't decrypt massage. This is encrypt only class.")


if __name__ == "__main__":
    a = Cipher()
    pprint.pprint(a.two_squares_list)

    b = Cipher(two_squares_list=a.two_squares_list)
    print(b.decrypt('imagine this string is encrypted'))