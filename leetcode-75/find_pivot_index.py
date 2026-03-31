class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1
        for _ in range(len(nums)):
            left_sum = sum(nums[:left])
            right_sum = sum(nums[right:])
            print(left, right, left_sum, right_sum, nums[:left], nums[right:])
            if left + 1 == right and left_sum == right_sum:
                return left

            if left_sum > right_sum:
                right -= 1
            if right_sum > left_sum:
                left += 1

            if right < left:
                break
        return -1
