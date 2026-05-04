# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverses a singly linked list in place.
        
        Time Complexity: O(N), where N is the number of nodes.
        Space Complexity: O(1).
        """
        prev: Optional[ListNode] = None
        curr: Optional[ListNode] = head
        
        # Explicit 'is not None' check is safer and more Pythonic for object comparisons
        while curr is not None:
            temp_next: Optional[ListNode] = curr.next
            curr.next = prev
            
            prev = curr
            curr = temp_next
            
        return prev
            