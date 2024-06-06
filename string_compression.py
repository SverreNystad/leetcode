class Solution:
    def compress(self, chars: list[str]) -> int:
        """
        Given an array of characters chars, compress it using the following algorithm:

        Begin with an empty string s. For each group of consecutive repeating characters in chars:

        If the group's length is 1, append the character to s.
        Otherwise, append the character followed by the group's length.
        The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

        After you are done modifying the input array, return the new length of the array.

        You must write an algorithm that uses only constant extra space.
        """

        s = ""
        current_letter: str = ""
        amount: int = 0

        start_range_index: int = 0
        end_range_index: int = 0

        for i in range(len(chars)):
            letter = chars[i]
            if current_letter == "":
                current_letter = letter

            if current_letter == letter:
                amount += 1
            else:
                if amount == 1:
                    s += current_letter
                else:
                    s += current_letter + str(amount)

                current_letter = letter
                amount = 1

        if amount == 1:
            s += current_letter
        else:
            s += current_letter + str(amount)

        # Mutate input variable
        for i in range(len(s)):
            chars[i] = s[i]

        for i in range(len(s), len(chars)):
            chars.pop()

        return len(s)


if __name__ == "__main__":
    s = Solution()
    input = ["a", "a", "b", "b", "c", "c", "c"]
    result = s.compress(input)
    assert result == 6
    assert input == "a2b2c3"
