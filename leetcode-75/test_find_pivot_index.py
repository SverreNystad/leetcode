from find_pivot_index import Solution


def test_solution():
    assert Solution().pivotIndex([1, 7, 3, 6, 5, 6]) == 3
    assert Solution().pivotIndex([1, 2, 3]) == -1
    assert Solution().pivotIndex([2, 1, -1]) == 0
