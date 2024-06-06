from move_zeros import Solution


def test_move_zero_with_non_zero_elements():
    s = Solution()
    input = [0, 1, 0, 3, 12]
    s.moveZeroes(input)
    expected_output = [1, 3, 12, 0, 0]
    assert input == expected_output


def test_move_zero_with_no_non_zero_elements():
    s = Solution()
    input = [0]
    s.moveZeroes(input)
    expected_output = [0]
    assert input == expected_output


def test_move_zero_with_no_zero_elements():
    s = Solution()
    input = [1]
    s.moveZeroes(input)
    expected_output = [1]
    assert input == expected_output
