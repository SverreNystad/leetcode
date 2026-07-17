from removing_stars_from_a_string import Solution


def test_solution():
    assert Solution().removeStars("leet**cod*e") == "lecoe"
    assert Solution().removeStars("erase*****") == ""
