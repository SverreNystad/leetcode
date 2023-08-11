import pytest

from string_compression import Solution

def test_string_compression():
    s = Solution()
    result = s.compress(["a","a","b","b","c","c","c"])
    assert result == 6

def test_string_compression_2():
    s = Solution()
    result = s.compress(["a"])
    assert result == 1

def test_string_compression_3():
    s = Solution()
    result = s.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"])
    assert result == 4