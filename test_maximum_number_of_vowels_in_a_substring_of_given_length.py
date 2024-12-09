from maximum_number_of_vowels_in_a_substring_of_given_length import Solution


def test_example1():
    s = "abciiidef"
    k = 3

    assert Solution().maxVowels(s, k) == 3


def test_example2():
    s = "aeiou"
    k = 2

    assert Solution().maxVowels(s, k) == 2


def test_example3():
    s = "leetcode"
    k = 3

    assert Solution().maxVowels(s, k) == 2
