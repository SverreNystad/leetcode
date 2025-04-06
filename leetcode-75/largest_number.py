from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        nums.sort(key=cmp_to_key(compare))

        # Edge case: if the largest number is '0', return '0'
        if nums[0] == "0":
            return "0"

        return "".join(nums)


def compare(x: str, y: str) -> int:
    if x + y > y + x:
        return -1
    elif x + y < y + x:
        return 1
    else:
        return 0
