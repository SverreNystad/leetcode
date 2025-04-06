class Solution:
    def merge_alternately(self, word1: str, word2: str) -> str:
        """
        You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
        If a string is longer than the other, append the additional letters onto the end of the merged string.

        Return the merged string.
        """
        merged = ""

        limit: int = min(len(word1), len(word2))
        longerWord = word2 if len(word1) <= len(word2) else word1

        for i in range(limit):
            merged += word1[i] + word2[i]

        # Add remaining part
        merged += longerWord[limit:]

        return merged
