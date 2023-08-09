import pytest
from can_place_flowers import Solution


def test_can_place_flowers1():
    flowerbed = [1, 0, 0, 0, 1]
    n = 1

    expected = True

    actual = Solution().can_place_flowers(flowerbed, n)
    assert actual == expected


def test_can_place_flowers2():
    flowerbed = [1, 0, 0, 0, 1]
    n = 2

    expected = False

    actual = Solution().can_place_flowers(flowerbed, n)
    assert actual == expected
