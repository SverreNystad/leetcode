from dataclasses import dataclass


class Solution:
    def increasing_triplet(self, nums: list[int]) -> bool:
        """
        Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. 
        If no such indices exists, return false.
        """
        
        first_min = float('inf')
        second_min = float('inf')

        for num in nums:
            if num <= first_min:
                first_min = num
            elif num <= second_min:
                second_min = num
            else:
                return True

        return False


