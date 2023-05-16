# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = ListNode(next=head)
        node = start
        while node:
            if node and node.next and node.next.next:
                first = node.next
                second = node.next.next
                first.next = second.next
                second.next = first
                node.next = second
                node = node.next.next
            else:
                return start.next
        return start.next