from unique_number_of_occurrences import Solution


def test_unique_number_of_occurrences_all_unique():
    x = [1, 2, 2, 1, 1, 3]
    assert Solution().uniqueOccurrences(x) == True


def test_non_unique_number_of_occurrences_():
    x = [1, 2]
    assert Solution().uniqueOccurrences(x) == False


def test_non_unique_number_of_occurrences_():
    x = [-1, -2]
    assert Solution().uniqueOccurrences(x) == False


def test_unique_number_of_occurrences_():
    x = []
    assert Solution().uniqueOccurrences(x) == True


def test_unique_number_of_occurrences_with_negative_numbers():
    x = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
    assert Solution().uniqueOccurrences(x) == True
