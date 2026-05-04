from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None) -> Optional[ListNode]:
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head:Optional[ListNode]) -> Optional[ListNode]:
        # traverse, in-place writing
        # store the next for keeping track of connections
        # connect current node to previous
        # move the pointer from prev to current, current to next.if not head:
        if not head:
            return None
        curr:ListNode = head
        prev:ListNode = None

        while curr is not None:
            next_temp = curr.next
            curr.next = prev

            prev = curr
            curr = next_temp
        return prev
