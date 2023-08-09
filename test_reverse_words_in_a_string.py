import pytest

from reverse_words_in_a_string import Solution


def test_reverse_words():
    s = "the sky is blue"

    expected = "blue is sky the"

    actual = Solution().reverse_words(s)
    assert actual == expected


def test_reverse_words_with_leading_spaces():
    s = "  hello world  "

    expected = "world hello"

    actual = Solution().reverse_words(s)
    assert actual == expected


def test_reverse_words_with_multiple_spaces():
    s = "a good   example"

    expected = "example good a"

    actual = Solution().reverse_words(s)
    assert actual == expected


def test_only_spaces():
    s = "  "

    expected = ""

    actual = Solution().reverse_words(s)
    assert actual == expected
