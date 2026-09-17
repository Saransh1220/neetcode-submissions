# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
     
       
        before = None
        t = head
        while t is not None:
            after = t.next
            t.next = before
            before = t
            t = after
        return before
            