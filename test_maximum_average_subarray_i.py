from maximum_average_subarray_i import Solution


def test_subarray_of_one():
    nums = [5]
    k = 1

    assert Solution().findMaxAverage(nums, k) == 5.0


def test_subarray_of_two_for_k():
    nums = [5, 10]
    k = 1

    assert Solution().findMaxAverage(nums, k) == 10.0


def test_negative_numbers():
    nums = [-1]
    k = 1

    assert Solution().findMaxAverage(nums, k) == -1.0


def test():
    nums = [1, 12, -5, -6, 50, 3]
    k = 4

    assert Solution().findMaxAverage(nums, k) == 12.75
