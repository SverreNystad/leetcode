from maximum_twin_sum_of_a_linked_list import Solution, ListNode
import pytest


@pytest.mark.parametrize(
    "head, expected",
    [
        (ListNode(5, ListNode(4, ListNode(2, ListNode(1)))), 6),
        (ListNode(4, ListNode(2, ListNode(2, ListNode(3)))), 7),
        (ListNode(1, ListNode(100000)), 100001),
    ],
)
def test_maximum_twin_sum_of_a_linked_list(head, expected):
    solution = Solution()
    assert solution.pairSum(head) == expected, (
        f"Expected {expected} but got {solution.pairSum(head)}"
    )
