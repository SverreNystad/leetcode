import pytest

from reverse_vowels_of_a_string import Solution


def test_reverse_vowels():
    s = "hello"

    expected = "holle"

    actual = Solution().reverse_vowels(s)
    assert actual == expected


def test_reverse_vowels_of_empty_string():
    s = ""

    expected = ""

    actual = Solution().reverse_vowels(s)
    assert actual == expected


def test_reverse_vowels_of_string_with_no_vowels():
    s = "bcdfghjklmnpqrstvwxyz"

    expected = "bcdfghjklmnpqrstvwxyz"

    actual = Solution().reverse_vowels(s)
    assert actual == expected


def test_reverse_vowels_of_string_with_one_vowel():
    s = "a"

    expected = "a"

    actual = Solution().reverse_vowels(s)
    assert actual == expected


def test_reveres_vowels_of_string_with_only_vowels():
    s = "aeiou"

    expected = "uoiea"

    actual = Solution().reverse_vowels(s)
    assert actual == expected
