class Solution:
    VOWELS = "aeiouAEIOU"

    def reverse_vowels(self, s: str) -> str:
        # Find vowels
        vowels = []
        for i in range(len(s)):
            if s[i] in Solution.VOWELS:
                vowels.append(s[i])

        # Return string with reversed vowels
        for i in range(len(s)):
            if s[i] in Solution.VOWELS:
                print(f"{s} {i} {vowels}")
                s = s[:i] + vowels.pop() + s[i + 1:]
        return s
