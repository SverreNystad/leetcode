class Solution:
    VOWELS = ("a", "e", "i", "o", "u")

    def maxVowels(self, s: str, k: int) -> int:
        max_vowels = 0

        for i in range(len(s) - k + 1):
            substring = s[i : i + k]
            vowels = sum(1 for char in substring if char in self.VOWELS)
            max_vowels = max(max_vowels, vowels)

        return max_vowels
