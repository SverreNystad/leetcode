from dataclasses import dataclass


class Solution:
    def increasing_triplet(self, nums: list[int]) -> bool:
        """
        Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 
        """
        all_triplets: list[Triplet] = []
        triplet_exists: bool = False
        for i in range(len(nums) - 2):
            for j in range(i+1, len(nums) -1):
                for k in range(j+1, len(nums)):
                    if nums[i] < nums[j] < nums[k]:
                        triplet_exists = True
                        all_triplets.append(Triplet(i, j, k))
        
        return triplet_exists

@dataclass(frozen=True)
class Triplet:
    i: int
    j: int
    k: int
    

