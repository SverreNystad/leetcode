# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next: ListNode | None = None):
        self.val: int = val
        self.next: ListNode | None = next

    def __repr__(self) -> str:
        output = ""
        current = self
        while current:
            output += f"{current.val}"
            current = current.next
        return output


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None

        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next

        return head
