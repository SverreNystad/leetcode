import pytest
from can_place_flowers import Solution


def test_can_place_flower():
    flowerbed = [1, 0, 0, 0, 1]
    n = 1

    expected = True

    actual = Solution().can_place_flowers(flowerbed, n)
    assert actual == expected


def test_cant_place_all_flowers():
    flowerbed = [1, 0, 0, 0, 1]
    n = 2

    expected = False

    actual = Solution().can_place_flowers(flowerbed, n)
    assert actual == expected


def tes_can_place_all_flowers():
    flowerbed = [0, 0, 0, 0]
    n = 2
    expected = True

    actual = Solution().can_place_flowers(flowerbed, n)
    assert actual == expected


def test_cant_place_flowers_in_empty_bed():
    flowerbed = []
    n = 1

    expected = False

    actual = Solution().can_place_flowers(flowerbed, n)
    assert actual == expected


def test_cant_place_flowers_in_bed_of_length_1():
    flowerbed = [1]
    n = 1

    expected = False

    actual = Solution().can_place_flowers(flowerbed, n)
    assert actual == expected


def test_can_place_flowers_in_bed_of_length_1():
    flowerbed = [1]
    n = 0

    expected = False

    actual = Solution().can_place_flowers(flowerbed, n)
    assert actual == expected


def test_can_place_flowers_in_bed_of_length_1():
    flowerbed = [0]
    n = 1

    expected = True

    actual = Solution().can_place_flowers(flowerbed, n)
    assert actual == expected


def can_plant_optimal_of_length_3():
    flowerbed = [0, 0, 0]
    n = 2

    expected = True

    actual = Solution().can_place_flowers(flowerbed, n)
    assert actual == expected
