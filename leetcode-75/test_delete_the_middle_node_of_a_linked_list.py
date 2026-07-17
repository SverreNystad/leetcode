from delete_the_middle_node_of_a_linked_list import Solution, ListNode

import pytest


@pytest.mark.parametrize(
    "head,expected",
    [
        (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), [1, 2, 4, 5]),
        (ListNode(1, ListNode(2, ListNode(3, ListNode(4)))), [1, 2, 4]),
        (ListNode(1, ListNode(2, ListNode(3))), [1, 3]),
        (ListNode(1), []),
    ],
)
def test_delete_middle_node(head, expected):
    solution = Solution()
    new_head = solution.deleteMiddle(head)

    # Convert the resulting linked list to a Python list for easy comparison
    result = []
    current = new_head
    while current:
        result.append(current.val)
        current = current.next

    assert result == expected, f"Expected {expected}, but got {result}"
