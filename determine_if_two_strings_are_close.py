class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """
        Two strings are considered close if you can attain one from the other using the following operations:
        * Operation 1: Swap any two existing characters.
            * For example, abcde -> aecdb
        * Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
            * For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)

        You can use the operations on either string as many times as necessary.
        """
        # Must be of same length
        if len(word1) != len(word2):
            return False

        # Contains the same amount of each letter
        letter_amounts_1 = self._count_letters(word1)
        letter_amounts_2 = self._count_letters(word2)

        if letter_amounts_1.keys() != letter_amounts_2.keys():
            return False

        return sorted(letter_amounts_1.values()) == sorted(letter_amounts_2.values())

    def _count_letters(self, word: set) -> dict[str, int]:
        letter_amounts = {}
        for c in word:
            if c in letter_amounts.keys():
                letter_amounts[c] = letter_amounts.get(c) + 1
            else:
                letter_amounts[c] = 1
        return letter_amounts
