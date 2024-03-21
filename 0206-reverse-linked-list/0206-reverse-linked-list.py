# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head
        next = None
        curr = None
        prev = None
        while start:
            if start:
                next = start.next
                start.next = prev
                prev = start
                start = next
        return prev