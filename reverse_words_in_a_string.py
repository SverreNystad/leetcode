class Solution:
    SEPARATORS = [" "]

    def reverse_words(self, s: str) -> str:
        """Given an input string s, reverse the order of the words.

        A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

        Return a string of the words in reverse order concatenated by a single space.

        Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
        """
        # Correct separators in string
        for separator in Solution.SEPARATORS:
            s.strip(separator)
            while separator*2 in s:
                s.replace(separator*2, separator)

        # Reverse words
        words: list[str] = []
        reversed = s
        for separator in Solution.SEPARATORS:
            words = reversed.split(separator)
            words.reverse()
            reversed = separator.join(words)
        return reversed
