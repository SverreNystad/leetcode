from max_consecutive_ones import Solution


def test_simple_case():
    s = Solution()
    assert s.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2) == 6


def test_another_case():
    s = Solution()
    assert s.longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0], 3) == 10
