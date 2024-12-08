from max_number_of_k_sum_pairs import Solution

# Input: nums = [1,2,3,4], k = 5
# Output: 2
# Explanation: Starting with nums = [1,2,3,4]:
# - Remove numbers 1 and 4, then nums = [2,3]
# - Remove numbers 2 and 3, then nums = []
# There are no more pairs that sum up to 5, hence a total of 2 operations.
# Example 2:
#
# Input: nums = [3,1,3,4,3], k = 6
# Output: 1
# Explanation: Starting with nums = [3,1,3,4,3]:
# - Remove the first two 3's, then nums = [1,4,3]
# There are no more pairs that sum up to 6, hence a total of 1 operation.


def test():
    nums = [1, 2, 3, 4]
    k = 5

    assert Solution().maxOperations(nums, k) == 2


def test2():
    nums = [3, 1, 3, 4, 3]
    k = 6

    assert Solution().maxOperations(nums, k) == 1


def test_all_numbers_larger_then_k():
    nums = [3, 3, 4, 3]
    k = 1

    assert Solution().maxOperations(nums, k) == 0
