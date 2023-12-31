import pytest

from merge_strings_alternately import Solution


def test_words_of_same_length():
    word1 = "abc"
    word2 = "pqr"

    expected = "apbqcr"

    actual = Solution().merge_alternately(word1, word2)
    assert actual == expected


def test_words_of_different_length1():
    word1 = "ab"
    word2 = "pqrs"

    expected = "apbqrs"

    actual = Solution().merge_alternately(word1, word2)
    assert actual == expected


def test_words_of_different_length2():
    word1 = "abcd"
    word2 = "pq"

    expected = "apbqcd"

    actual = Solution().merge_alternately(word1, word2)
    assert actual == expected
