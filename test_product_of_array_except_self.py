import pytest

from product_of_array_except_self import Solution


def test_only_positive():
    s = Solution()
    result = s.product_except_self([1, 2, 3, 4])
    assert result == [24, 12, 8, 6]


def test_only_negative():
    s = Solution()
    result = s.product_except_self([-1, -2, -3, -4])
    assert result == [-24, -12, -8, -6]


def test_mixed():
    s = Solution()
    result = s.product_except_self([-1, 2, -3, 4])
    assert result == [-24, 12, -8, 6]
