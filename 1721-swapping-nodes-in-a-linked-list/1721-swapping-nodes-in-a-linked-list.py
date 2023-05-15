# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start = ListNode(next=head)
        node = start
        counter = 0
        first = None
        gap = 0
        end = node
        while node:
            if counter==k-1:
                first=node
            counter+=1
            if gap>=k+1:
                end = end.next
            gap+=1
            node = node.next
        if first == end:
            return start.next
        first.next ,end.next = end.next, first.next
        first.next.next, end.next.next = end.next.next, first.next.next 
        return start.next
        
                    