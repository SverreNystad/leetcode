import pytest

from increasing_triplet_subsequence import Solution

def test_increasing_triplet():
    s = Solution()
    result = s.increasing_triplet([1, 2, 3, 4, 5])
    assert result == True

def test_not_increasing_triplet():
    s = Solution()
    result = s.increasing_triplet([5, 4, 3, 2, 1])
    assert result == False

def test_increasing_triplet_with_duplicates():
    s = Solution()
    result = s.increasing_triplet([1, 2, 2, 3, 4, 5])
    assert result == True

def test_to_small_list():
    s = Solution()
    result = s.increasing_triplet([1, 2])
    assert result == False

def test_negative_numbers():
    s = Solution()
    result = s.increasing_triplet([0,4,2,1,0,-1,-3])
    assert result == False

def test_several_solution():
    s = Solution()
    result = s.increasing_triplet([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
    assert result == True

def test_():
    s = Solution()
    result = s.increasing_triplet([2,1,5,0,4,6])
    assert result == True