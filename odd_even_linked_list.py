from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_link: ListNode = None
        even_link: ListNode = None

        index = 0
        current = head
        while current.next:
            
            right = current.next
            if index % 2 == 0:
                odd_link = current
                if current.next.next:
                    current.next = current.next.next
            else:
                even_link = current
                if current.next.next:
                    current.next = current.next.next

            current = right
            index += 1

        odd_link.next = even_link
        return head

    
