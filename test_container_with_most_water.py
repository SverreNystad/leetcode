from container_with_most_water import Solution


def test_when_choice_requires_to_not_take_the_two_largest():
    s = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    output = s.maxArea(height)
    expected = 49
    assert output == expected


def test_simplest_solution():
    s = Solution()
    height = [0, 0]
    output = s.maxArea(height)
    expected = 0
    assert output == expected


def test_simplest_solution():
    s = Solution()
    height = [1, 1]
    output = s.maxArea(height)
    expected = 1
    assert output == expected


def test_no_height():
    s = Solution()
    height = []
    try:
        s.maxArea(height)
    except ValueError:
        assert True


def test_only_one_height():
    s = Solution()
    height = [1]
    try:
        s.maxArea(height)
        assert False
    except ValueError:
        assert True


def test_negative_height_values():
    s = Solution()
    height = [-1, 1]
    try:
        s.maxArea(height)
        assert False
    except ValueError:
        assert True
