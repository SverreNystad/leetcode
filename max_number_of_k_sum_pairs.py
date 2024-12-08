from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        operations = 0

        # Create a dictionary to store the frequency of each number

        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # Iterate through the dictionary and check if the complement of the current number exists in the dictionary
        # If it does, increment the operations count and decrement the frequency of the current number and its complement
        for num in freq:
            complement = k - num
            if complement in freq:
                if complement == num:
                    operations += freq[num] // 2
                else:
                    operations += min(freq[num], freq[complement])
                    freq[num] = 0
                    freq[complement] = 0
        return operations
