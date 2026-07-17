from dota2_senate import Solution
import pytest


@pytest.mark.parametrize(
    "input,expected",
    [
        ("R", "Radiant"),
        ("RDR", "Radiant"),
        ("RD", "Radiant"),
        ("RDD", "Dire"),
        ("DRR", "Radiant"),
        ("RDDDDDDDDDDDDDDDDD", "Dire"),
        ("RRRDDD", "Radiant"),
        ("DDRRR", "Dire"),
        ("DRRD", "Dire"),
        ("RDDR", "Radiant"),
        ("DRRDRDRDRDDRDRDR", "Radiant"),
    ],
)
def test_first_senator_bans_second(input, expected):

    actual = Solution().predictPartyVictory(input)

    assert actual == expected
