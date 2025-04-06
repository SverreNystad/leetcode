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

        # Correct alphabet
        s1 = sorted(set(word1))
        s2 = sorted(set(word2))

        if s1 != s2:
            return False

        counts_1 = self._count_letters(word1, s1)
        counts_2 = self._count_letters(word2, s2)

        return sorted(counts_1) == sorted(counts_2)

    def _count_letters(self, word: str, alphabet: set[str]) -> list[int]:
        counts = []
        for letter in alphabet:
            counts.append(word.count(letter))
        return counts
