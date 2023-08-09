class Solution:
    def gcd_of_strings(self, str1: str, str2: str) -> str:
        """
        For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).
        Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2
        """
        if not _exists_gcd(str1, str2):
            return ""

        gcd = self._gcd(len(str1), len(str2))
        gcd_str = str1[:gcd]
        return gcd_str


def _gcd(a: int, b: int) -> int:
    """
    Euclidean algorithm:
    Denoting this remainder as a mod b, the algorithm replaces (a, b) by (b, a mod b) repeatedly until the pair is (d, 0), where d is the greatest common divisor.
    """
    if b == 0:
        return a
    return _gcd(b, a % b)


def _exists_gcd(str1: str, str2: str) -> bool:
    """
    Check if a gcd exists
    """
    return str1 + str2 == str2 + str1
# AKA: Greatest Common Divisor of Strings:
# The word must only contain the gcd cant contain other characters
