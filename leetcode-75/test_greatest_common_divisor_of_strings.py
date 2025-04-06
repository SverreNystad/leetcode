import pytest
from greatest_common_divisor_of_strings import Solution


def test_gcd_of_strings():
    str1 = "ABCABC"
    str2 = "ABC"

    expected = "ABC"

    actual = Solution().gcd_of_strings(str1, str2)
    assert actual == expected


def test_gcd_of_strings2():
    str1 = "ABABAB"
    str2 = "ABAB"

    expected = "AB"

    actual = Solution().gcd_of_strings(str1, str2)
    assert actual == expected


def test_gcd_of_with_no_gcd():
    str1 = "LEET"
    str2 = "CODE"

    expected = ""

    actual = Solution().gcd_of_strings(str1, str2)
    assert actual == expected
