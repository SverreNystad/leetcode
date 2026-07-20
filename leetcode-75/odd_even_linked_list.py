from typing import Optional


# Definition for singly-linked list.
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


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        odd_current = head
        even_head = head.next
        even_current = head.next

        while even_current and even_current.next:
            # Connect current odd node to next odd node
            odd_current.next = even_current.next
            odd_current = odd_current.next
            # Connect current even node to next even node
            even_current.next = odd_current.next
            even_current = even_current.next

        odd_current.next = even_head
        return head
