from odd_even_linked_list import Solution, ListNode

import pytest


@pytest.mark.parametrize(
    "head,expected",
    [
        (
            ListNode(
                1,
                ListNode(
                    2,
                    ListNode(
                        3,
                        ListNode(
                            4,
                            ListNode(
                                5, ListNode(6, ListNode(7, ListNode(8, ListNode(9))))
                            ),
                        ),
                    ),
                ),
            ),
            [1, 3, 5, 7, 9, 2, 4, 6, 8],
        ),
        (
            ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))),
            [1, 3, 5, 2, 4],
        ),
        (ListNode(1, ListNode(2, ListNode(3, ListNode(4)))), [1, 3, 2, 4]),
        (ListNode(1, ListNode(2, ListNode(3))), [1, 3, 2]),
        (ListNode(1), [1]),
    ],
)
def test_odd_even_list(head, expected):
    solution = Solution()
    new_head = solution.oddEvenList(head)

    # Convert the resulting linked list to a Python list for easy comparison
    result = []
    current = new_head
    while current:
        result.append(current.val)
        current = current.next

    assert result == expected, f"Expected {expected}, but got {result}"
