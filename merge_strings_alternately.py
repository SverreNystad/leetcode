class Solution:
    def merge_alternately(self, word1: str, word2: str) -> str:
        """
        You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
        If a string is longer than the other, append the additional letters onto the end of the merged string.

        Return the merged string.
        """
        merge = ""

        _max: int = max(len(word1), len(word2))
        for i in range(_max):
            merge += word1[i]
            merge += word2[i]
        return merge
