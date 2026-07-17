# Definition for singly-linked list.
from typing import Optional
from math import floor


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


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # find length of list take modulo and remove the middle
        # requires either

        current = head
        if not current.next:
            return None

        length = 0
        while current:
            current = current.next
            length += 1

        middle_index = floor(length / 2)
        index = 0
        current = head
        while current:
            # remove before and after

            if index == middle_index - 1:
                last = current

                if current.next.next:
                    last.next = current.next.next
                else:
                    last.next = None
            index += 1
            current = current.next
        return head
        # when no clean middle remove the one to the right
