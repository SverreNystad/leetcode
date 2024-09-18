from determine_if_two_strings_are_close import Solution


def test_determine_swap_possible():
    word1 = "abc"
    word2 = "bca"
    assert Solution().closeStrings(word1, word2) == True


def test_determine_not_enough_letters():
    word1 = "a"
    word2 = "aa"
    assert Solution().closeStrings(word1, word2) == False


def test_determine_transform_possible_1():
    word1 = "cabbba"
    word2 = "abbccc"
    assert Solution().closeStrings(word1, word2) == True


def test_determine_transform_possible_same():
    word1 = "eecaab"
    word2 = "eecbaa"
    # aab
    # baa
    assert Solution().closeStrings(word1, word2) == True


def test_determine_transform_possible_same_1():
    word1 = "ecaab"
    word2 = "dcabb"
    # aab
    # baa
    assert Solution().closeStrings(word1, word2) == False


def test_determine_transform_possible_2():
    word1 = "aacabb"
    word2 = "bbcbaa"
    assert Solution().closeStrings(word1, word2) == True


def test_determine_transform_possible_3():
    word1 = "uau"
    word2 = "ssx"
    assert Solution().closeStrings(word1, word2) == False
