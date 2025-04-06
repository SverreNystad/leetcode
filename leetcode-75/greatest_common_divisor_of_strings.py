import math


class Solution:
    def gcd_of_strings(self, str1: str, str2: str) -> str:
        """
        For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).
        Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2
        """
        # Exits early if there is no GCD
        if str1 + str2 != str2 + str1:
            return ""
        # Finds the GCD string
        gcd = math.gcd(len(str1), len(str2))
        return str1[:gcd]
