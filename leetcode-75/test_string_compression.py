import pytest

from string_compression import Solution


def test_string_compression_multiple_of_several_letters():
    s = Solution()
    input = ["a", "a", "b", "b", "c", "c", "c"]
    result = s.compress(input)
    assert result == 6
    assert input == ["a", "2", "b", "2", "c", "3"]


def test_string_compression_single_letter():
    s = Solution()
    input = ["a"]
    result = s.compress(input)
    assert result == 1
    assert input == ["a"]


def test_string_compression_many_of_same():
    s = Solution()
    input = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    result = s.compress(input)
    assert result == 4
    assert input == ["a", "b", "1", "2"]
