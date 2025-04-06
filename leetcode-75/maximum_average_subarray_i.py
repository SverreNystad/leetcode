from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_average = float("-inf")
        for i in range(len(nums) - k + 1):
            max_average = max(max_average, sum(nums[i : i + k]))
        return max_average / k
