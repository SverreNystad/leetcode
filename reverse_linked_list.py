from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next: "ListNode" =None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        new_list = None
        current = head
        
        while current:
            right = current.next
            current.next = new_list
            new_list = current
            current = right
        

        return new_list


