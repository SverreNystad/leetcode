class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
        A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters.
        (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
        """
        # Early escape
        if len(s) == 0:
            return True

        if len(t) <= len(s):
            return False

        i = 0
        wanted_letter = s[i]
        for letter in t:
            if letter == wanted_letter:
                i += 1
                if i == len(s):
                    return True
                wanted_letter = s[i]

        return False
