from dota2_senate import Solution
import pytest


@pytest.mark.parametrize(
    "input,expected",
    [
        ("R", "Radiant"),
        ("RD", "Radiant"),
        ("RDD", "Dire"),
        ("RRRDDD", "Radiant"),
        ("DDRRR", "Dire"),
    ],
)
def test_first_senator_bans_second(input, expected):

    actual = Solution().predictPartyVictory(input)

    assert actual == expected
