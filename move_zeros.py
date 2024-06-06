class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        self.move_token(nums, 0)

    def move_token(self, nums: list[int], token: int) -> None:
        amount_of_tokens_found: int = 0
        i: int = 0

        while i < len(nums) - amount_of_tokens_found:
            if nums[i] == token:
                nums.pop(i)
                nums.append(token)
                amount_of_tokens_found += 1
                continue
            i += 1


if __name__ == "__main__":
    s = Solution()
    input = [0, 1, 0, 3, 12]
    s.moveZeroes(input)
    expected_output = [1, 3, 12, 0, 0]
    assert input == expected_output
