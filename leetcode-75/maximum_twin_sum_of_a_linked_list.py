# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        output = ""
        current = self
        while current:
            output += f"{current.val}"
            current = current.next
        return output


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        max_sum = 0
        # Find middle of the linked list
        middle_node: ListNode = self._find_middle(head)
        # Reverse the second half of the linked list
        reversed_right_part: ListNode = self._reverse_list(middle_node)
        left_part = head
        while left_part and reversed_right_part:
            current = left_part.val + reversed_right_part.val
            if current >= max_sum:
                max_sum = current
            left_part = left_part.next
            reversed_right_part = reversed_right_part.next

        return max_sum

    def _find_middle(self, head: ListNode) -> ListNode:
        """
        Find the middle node of a linked list using the slow and fast pointer technique.
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def _reverse_list(self, head: ListNode) -> ListNode:

        new_list = None
        current = head

        while current:
            right = current.next
            current.next = new_list
            new_list = current
            current = right

        return new_list
