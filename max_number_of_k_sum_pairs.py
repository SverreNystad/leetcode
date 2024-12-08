from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        operations = 0

        left = 0
        right = len(nums) - 1
        nums.sort()
        while left < right:
            if nums[left] + nums[right] == k:
                left += 1
                right -= 1
                operations += 1

            elif nums[left] + nums[right] > k:
                right -= 1

            else:
                left += 1
        return operations
