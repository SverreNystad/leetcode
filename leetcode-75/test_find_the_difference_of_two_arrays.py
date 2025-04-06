from find_the_difference_of_two_arrays import Solution


def test_find_difference():
    nums1 = [1, 2, 3]
    nums2 = [2, 4, 6]

    solution = Solution()
    assert solution.findDifference(nums1, nums2) == [[1, 3], [4, 6]]
