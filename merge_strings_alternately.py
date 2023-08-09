class Solution:
    def merge_alternately(self, word1: str, word2: str) -> str:
        """
        You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
        If a string is longer than the other, append the additional letters onto the end of the merged string.
        Return the merged string.
        """
        merged = []
        for w1, w2 in zip(word1, word2):
            merged.extend([w1, w2])

        # Add remaining
        _min: int = min(len(word1), len(word2))
        if len(word1) <= len(word2):
            merged.extend(word2[_min:])
        else:
            merged.extend(word1[_min:])
        return ''.join(merged)
