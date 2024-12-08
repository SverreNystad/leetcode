from typing import List

from numpy import mean


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        all_subarrays = []
        for i in range(len(nums) - k + 1):
            all_subarrays.append(nums[i : i + k])

        max_average = float("-inf")
        for subarray in all_subarrays:
            average = mean(subarray)
            if average > max_average:
                max_average = average
        return max_average
