from string import ascii_lowercase as alphabet
from typing import List


class PermutationCipher:
    def __init__(self, first_keyword:str='abstract', second_keyword:str='word', phrase:str='my phrase to encrypt or decrypt'):
        self.first_keyword = first_keyword.strip()
        self.second_keyword = second_keyword.strip()
        self.phrase = phrase.strip()
        self.origin_matrix = self._matrix_from_keywords_and_phrase()
        self._remove_empety_rows()
        self.permutate_matrix = self._matrix_double_permutate()

    def _is_row_empty(self, row_num:int) -> bool:
        """ Condition method. Return True, if all chars in row is empty strings (except for 0 element).

        Args:
            row_num (int): row number in the matrix.

        Raises:
            IndexError: raise if row_number refers to a non-existent index of origin matrix.

        Returns:
            bool: True, if all chars in row is empty strings (except for 0 element), else False.
        """
        try:
            return all(True if x == ' ' else False for x in self.origin_matrix[row_num][1:])
        except IndexError:
            return False

    def _remove_empety_rows(self) -> None:
        """ Remove all rows, that consists of empty strings. 
        
        Example: ['d', '', '', '', ''] # all elements in slice list[1:] are empty.
                 First element is not considered, cause it always not em 
        
         """
        for row_num in range(1, len(self.origin_matrix)+1):
            if self._is_row_empty(row_num):
                del self.origin_matrix[row_num]
        self.second_keyword = ''.join(self.origin_matrix[x][0] for x in range(1, len(self.origin_matrix)))

    def _matrix_from_keywords_and_phrase(self) -> List[List[str]]:
        """ Generate matrix by first_keyword row and second_keyword column and phrase matrix. 

        Returns:
            List[List[str]]: matrix.
        """        
        matrix = [[0 for _ in range(len(self.first_keyword)+1)] for _ in range(len(self.second_keyword)+1)]
        matrix[0][0] = '' # unusing field

        # first keyword insert
        first_keyword_iter = iter(self.first_keyword)
        for x in range(1, len(self.first_keyword)+1):
            matrix[0][x] = next(first_keyword_iter)

        # second keyword insert
        second_keyword_iter = iter(self.second_keyword)
        for y in range(1, len(self.second_keyword)+1):
            matrix[y][0] = next(second_keyword_iter)

        # phrase insert
        phrase_iter = iter(self.phrase)
        for y in range(1, len(self.second_keyword)+1):
            for x in range(1, len(self.first_keyword)+1):
                try:
                    matrix[y][x] = next(phrase_iter)
                except StopIteration:
                    matrix[y][x] = ' '

        return matrix

    def _matrix_double_permutate(self) -> List[List[str]]:
        """ Generate matrix by permutate rows and columns in alphabetical order
        in origin matrix.

        Returns:
            List[List[str]]: matrix.
        """
        matrix = [self.origin_matrix[0]] + sorted(self.origin_matrix[1:], key=lambda x: x[0])
        double_permutate_right_slice = sorted([*zip(*[row[1:] for row in matrix])], key=lambda x: x[0])
        double_permutate_left_slice = [x[0] for x in matrix]

        double_permutate_right_slice = [list(x) for x in [*zip(*double_permutate_right_slice)]]

        return [[double_permutate_left_slice[i]] + double_permutate_right_slice[i] for i in range(len(self.second_keyword)+1)]

    def encrypting(self) -> str:
        """ Main method. Encrypt input string by double permutation cipher.

        Returns:
            str: enctypted string.
        """
        encrypt_phrase_as_matrix = [row[1:] for row in self.permutate_matrix[1:]]
        return ''.join([str(x) for y in encrypt_phrase_as_matrix for x in y])

    def decrypting(self) -> str:
        """ Main method. Decrypt input string by double permutation cipher.

        Returns:
            str: decrypted string.
        """        
        decrypt_phrase_as_matrix = [row[1:] for row in self.origin_matrix[1:]]
        return ''.join([str(x) for y in decrypt_phrase_as_matrix for x in y])


if __name__ == "__main__":
    cipher = PermutationCipher('abstract', 'word', 'abstractt')
    print(*cipher.origin_matrix, '\n', sep='\n')
    print(*cipher.permutate_matrix, sep='\n')
    print(cipher.encrypting())
    print(cipher.decrypting())