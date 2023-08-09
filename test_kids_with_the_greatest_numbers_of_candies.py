import pytest
from kids_with_the_greatest_numbers_of_candies import Solution


def test_kids_with_candies():
    candies = [2, 3, 5, 1, 3]
    extra_candies = 3

    expected = [True, True, True, False, True]

    actual = Solution().kids_with_candies(candies, extra_candies)
    assert actual == expected


def test_kids_with_candies2():
    candies = [4, 2, 1, 1, 2]
    extra_candies = 1

    expected = [True, False, False, False, False]

    actual = Solution().kids_with_candies(candies, extra_candies)
    assert actual == expected


def test_kids_with_candies3():
    candies = [12, 1, 12]
    extra_candies = 10

    expected = [True, False, True]

    actual = Solution().kids_with_candies(candies, extra_candies)
    assert actual == expected
