from is_subsequence import Solution


def test_empty_sub_string():
    solution = Solution()
    s = ""
    t = "abc"
    assert solution.isSubsequence(s, t)


def test_subsequence_in_sequence():
    solution = Solution()
    s = "abc"
    t = "ahbgdc"
    assert solution.isSubsequence(s, t)


def test_subsequence_not_in_sequence():
    solution = Solution()
    s = "axc"
    t = "ahbgdc"
    assert not solution.isSubsequence(s, t)
