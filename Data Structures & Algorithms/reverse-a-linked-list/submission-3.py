from typing import Optional

class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class Solution:
    def reverseList(self, head=Optional[ListNode]) -> Optional[ListNode]:
        # two pointers
        # store the next temporary head
        # connect the current to the previous node (None for initial case)
        # move the previous pointer to current
        # move the current pointer to next
        curr = head
        prev = None
        while curr is not None:
            temp = curr.next
            curr.next = prev
            
            prev = curr
            curr = temp
        return prev
        